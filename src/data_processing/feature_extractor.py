"""Reusable feature extractors used by NewsBot classifiers."""
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

def tfidf_features(max_features=12000):
    """Return the midterm-style word TF-IDF feature extractor."""
    return TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_features=max_features)

def count_features(max_features=6000):
    """Return a count vectorizer suitable for LDA topic modeling."""
    return CountVectorizer(stop_words='english', max_features=max_features, min_df=2, max_df=.95)
