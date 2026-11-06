"""Small stateful conversational interface with source-grounded follow-ups."""
from src.conversation.intent_classifier import IntentClassifier
class ConversationalInterface:
    def __init__(self,engine):
        self.engine=engine
        self.intent=IntentClassifier()
        self.selected_index=None
    def ask(self,query):
        if not isinstance(query,str) or not query.strip():
            return {'error':'Query must be nonempty'}
        intent=self.intent.classify(query)
        if intent=='search':
            results=self.engine.search(query,top_k=5)
            if results:self.selected_index=results[0]['index']
            return {'intent':intent,'results':results,'selected_article_id':self.selected_index}
        if self.selected_index is None or not 0<=self.selected_index<len(self.engine.df):
            return {'intent':intent,'error':'Search for an article first.'}
        article=self.engine.df.iloc[self.selected_index]['text']
        if intent=='summarize':return {'intent':intent,'summary':self.engine.summarize(article)}
        if intent=='entities':return {'intent':intent,'entities':self.engine.entities(article)}
        if intent=='sentiment':return {'intent':intent,'sentiment':self.engine.sentiment(article)}
        if intent=='translate':return {'intent':intent,'translation':self.engine.translate(article[:1500],'en','vi')}
        return {'intent':intent,'error':'Unsupported intent'}
