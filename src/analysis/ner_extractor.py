from collections import Counter
import networkx as nx
class EntityExtractor:
    def __init__(self,model='en_core_web_sm'):
        import spacy
        try:self.nlp=spacy.load(model)
        except OSError:raise RuntimeError('Install spaCy model: python -m spacy download en_core_web_sm')
    def extract(self,text):
        return [{'text':e.text,'label':e.label_,'start':e.start_char,'end':e.end_char} for e in self.nlp(text).ents]
    def cooccurrence(self,texts,max_articles=300):
        g=nx.Graph()
        for doc in self.nlp.pipe(list(texts)[:max_articles],batch_size=24):
            names=list(dict.fromkeys(e.text for e in doc.ents if e.label_ in {'PERSON','ORG','GPE'}))[:25]
            for i,a in enumerate(names):
                for b in names[i+1:]:
                    g.add_edge(a,b,weight=g.get_edge_data(a,b,{}).get('weight',0)+1)
        return g
