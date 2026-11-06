import re
class IntentClassifier:
    def classify(self,query):
        q=query.lower()
        if any(w in q for w in ('translate','vietnamese','dịch')):return 'translate'
        if any(w in q for w in ('summarize','summary','tóm tắt')):return 'summarize'
        if any(w in q for w in ('entity','entities','organization','people mentioned')):return 'entities'
        if any(w in q for w in ('sentiment','positive','negative','tone')):return 'sentiment'
        return 'search'
