import pytest
pytest.importorskip("langdetect")
from src.multilingual.cross_lingual_analyzer import CrossLingualAnalyzer
from src.multilingual.language_detector import LanguageDetector
class FakeSearch:
    def search(self,query,top_k=5,indices=None):return {'query':query,'indices':indices}

def test_language_short_text():
    assert LanguageDetector().detect('hi')=='unknown'

def test_filter_requires_metadata():
    with pytest.raises(ValueError):CrossLingualAnalyzer(FakeSearch()).compare('news',language='vi')

def test_filter_uses_language():
    analyzer=CrossLingualAnalyzer(FakeSearch(),[{'language':'en'},{'language':'vi'}])
    assert analyzer.compare('news',language='vi')['indices']==[1]
