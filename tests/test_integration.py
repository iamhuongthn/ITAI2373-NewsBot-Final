from src.conversation.interface import ConversationalInterface
import pandas as pd
class FakeEngine:
    df=pd.DataFrame({'text':['The economy and stock market gained today.']})
    def search(self,q,top_k=5):return [{'index':0,'text':self.df.iloc[0]['text'],'score':.9}]
    def summarize(self,t):return 'Market gained.'
    def entities(self,t):return []
    def sentiment(self,t):return {'label':'positive'}
    def translate(self,t,source,target):return 'Thị trường tăng.'

def test_conversation_context():
    bot=ConversationalInterface(FakeEngine())
    assert 'error' in bot.ask('summarize')
    assert bot.ask('market news')['selected_article_id']==0
    assert bot.ask('summarize')['summary']=='Market gained.'
    assert bot.ask('sentiment')['sentiment']['label']=='positive'
