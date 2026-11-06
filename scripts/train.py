import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from config.settings import DATASET,MODEL
from src.engine import NewsBotEngine
if __name__=='__main__':
    engine=NewsBotEngine(DATASET,MODEL)
    print('Articles:',len(engine.df),'Saved classifier:',MODEL)
    if hasattr(engine,'metrics'):print('Evaluation:',engine.metrics['accuracy'],engine.metrics['macro_f1'])
    engine.initialize_topics(n_topics=7,method='lda')
    for i in range(7):print('LDA topic',i,engine.topic_modeler.get_topic_words(i))
