import os
from pathlib import Path
from flask import Flask,render_template,request,jsonify,session
from config.settings import DATASET,MODEL
from src.engine import NewsBotEngine
from src.conversation.interface import ConversationalInterface

app=Flask(__name__)
app.secret_key=os.environ.get('SECRET_KEY','local-demo-only-change-before-deployment')
engine=None

def get_engine():
    global engine
    if engine is None:
        if not DATASET.exists():raise FileNotFoundError('Missing BBC dataset. Run python scripts/setup_data.py')
        engine=NewsBotEngine(DATASET,MODEL)
    return engine

@app.route('/')
def home():return render_template('index.html')

@app.route('/api/health')
def health():return jsonify({'status':'ok','dataset_available':DATASET.exists()})

@app.route('/api/analyze',methods=['POST'])
def analyze():
    try:
        payload=request.get_json(silent=True) or {}
        return jsonify(get_engine().analyze(str(payload.get('text','')),bool(payload.get('summarize',False))))
    except (ValueError,FileNotFoundError) as e:return jsonify({'error':str(e)}),400
    except Exception:
        app.logger.exception('Analysis failed');return jsonify({'error':'Analysis failed. Check server logs.'}),500

@app.route('/api/query',methods=['POST'])
def query():
    try:
        payload=request.get_json(silent=True) or {}
        q=str(payload.get('query','')).strip()
        if not q:return jsonify({'error':'Query is required'}),400
        bot=ConversationalInterface(get_engine())
        bot.selected_index=session.get('selected_index')
        response=bot.ask(q)
        session['selected_index']=bot.selected_index
        return jsonify(response)
    except Exception:
        app.logger.exception('Query failed');return jsonify({'error':'Query failed. Check server logs.'}),500

if __name__=='__main__':app.run(host='127.0.0.1',port=int(os.environ.get('PORT','5000')),debug=False)
