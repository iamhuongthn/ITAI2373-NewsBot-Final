from src.analysis.topic_modeler import TopicModeler
import pytest
DOCS=['space rocket nasa moon launch mission','rocket astronauts space exploration mission',
'football match stadium team scores','football coach player match win',
'bank market shares investment economy','finance bank stock market economy',
'space satellite mission nasa scientists','stadium player football tournament',
'stock exchange shares investment growth']
@pytest.mark.parametrize('method',['lda','nmf'])
def test_topics(method):
    model=TopicModeler(n_topics=3,method=method)
    weights=model.fit_transform(DOCS)
    assert weights.shape==(len(DOCS),3)
    assert len(model.get_topic_words(0))>0
    assert len(model.get_article_topics(DOCS[0]))==3

def test_invalid_method():
    with pytest.raises(ValueError):TopicModeler(method='unsupported')
