from src.conversation.intent_classifier import IntentClassifier
class QueryProcessor:
    def __init__(self):self.intents=IntentClassifier()
    def process(self,query):
        return {'intent':self.intents.classify(query),'query':query.strip()}
