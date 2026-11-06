from pathlib import Path
from src.data_processing.data_validator import load_bbc
from src.analysis.classifier import NewsClassifier
from src.analysis.topic_modeler import TopicModeler
from src.analysis.sentiment_analyzer import SentimentAnalyzer
from src.multilingual.language_detector import LanguageDetector

class NewsBotEngine:
    def __init__(self,dataset,model_path=None,load_heavy=False):
        self.df=load_bbc(dataset)
        self.classifier=NewsClassifier.load(model_path) if model_path and Path(model_path).exists() else NewsClassifier()
        if not (model_path and Path(model_path).exists()):
            self.metrics=self.classifier.train(self.df)
            if model_path:self.classifier.save(model_path)
        self.sentiment_engine=SentimentAnalyzer();self.language=LanguageDetector()
        self.topic_modeler=None;self.search_engine=None;self.summarizer=None;self.ner=None;self.translator=None
        if load_heavy:self.initialize_search()
    def initialize_topics(self,n_topics=7,method='lda'):
        self.topic_modeler=TopicModeler(n_topics,method)
        self.topic_modeler.fit_transform(self.df.text.tolist())
    def initialize_search(self):
        from src.language_models.embeddings import SemanticSearchEngine
        self.search_engine=SemanticSearchEngine();self.search_engine.index(self.df.text.tolist())
    def search(self,query,top_k=5):
        if self.search_engine is None:self.initialize_search()
        return self.search_engine.search(query,top_k)
    def summarize(self,text):
        if self.summarizer is None:
            from src.language_models.summarizer import IntelligentSummarizer
            self.summarizer=IntelligentSummarizer()
        return self.summarizer.summarize(text)
    def sentiment(self,text):return self.sentiment_engine.analyze(text)
    def entities(self,text):
        if self.ner is None:
            from src.analysis.ner_extractor import EntityExtractor
            self.ner=EntityExtractor()
        return self.ner.extract(text)
    def translate(self,text,source='en',target='vi'):
        if self.translator is None:
            from src.multilingual.translator import Translator
            self.translator=Translator()
        return self.translator.translate(text,source,target)
    def analyze(self,text,include_summary=False):
        if len(text.strip())<15:raise ValueError('Please provide at least 15 characters.')
        out={'classification':self.classifier.predict(text),'sentiment':self.sentiment(text),'language':self.language.detect(text),'entities':self.entities(text)}
        if self.topic_modeler:out['topics']=self.topic_modeler.get_article_topics(text)
        if include_summary:out['summary']=self.summarize(text)
        return out
