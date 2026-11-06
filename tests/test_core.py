import pandas as pd
from src.data_processing.text_preprocessor import clean_text
from src.data_processing.data_validator import load_bbc
from src.analysis.topic_modeler import TopicModeler
from src.conversation.intent_classifier import IntentClassifier

def test_clean():assert clean_text('Hello  \n world')=='Hello world'
def test_intents():
    ic=IntentClassifier()
    assert ic.classify('summarize this article')=='summarize'
    assert ic.classify('find business news')=='search'
def test_data(tmp_path):
    f=tmp_path/'bbc.csv';pd.DataFrame({'Text':['hello world','hello world','technology grows'],'Category':['tech','tech','business']}).to_csv(f,index=False)
    assert len(load_bbc(f))==2
def test_topics():
    docs=['football team wins the match','football team scores goals','business stocks market rises','business market shares fall','computer software technology advances','technology computer software updates']
    model=TopicModeler(2,'nmf');weights=model.fit_transform(docs)
    assert weights.shape==(6,2)
    assert len(model.get_topic_words(0))>0
