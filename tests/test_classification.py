from src.analysis.classifier import NewsClassifier
import pandas as pd

def test_classifier_training_and_prediction():
    docs=[]
    for category,stem in [('tech','software computer internet'),('sport','football stadium team')]:
        for i in range(12):docs.append({'text':f'{stem} report number {i}', 'category':category})
    model=NewsClassifier()
    metrics=model.train(pd.DataFrame(docs))
    assert 0<=metrics['accuracy']<=1
    pred=model.predict('software computer internet')
    assert pred['category'] in ('tech','sport')
    assert 'estimated_probability' in pred
