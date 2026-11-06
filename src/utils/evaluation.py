"""Metrics utilities. Never report illustrative values as measured results."""
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

def classification_metrics(y_true, y_pred):
    return {
        'accuracy': float(accuracy_score(y_true,y_pred)),
        'macro_precision': float(precision_score(y_true,y_pred,average='macro',zero_division=0)),
        'macro_recall': float(recall_score(y_true,y_pred,average='macro',zero_division=0)),
        'macro_f1': float(f1_score(y_true,y_pred,average='macro',zero_division=0)),
    }

def precision_at_k(relevant_ids, retrieved_ids, k=5):
    """Evaluate retrieval using independently labeled relevance judgments."""
    if k<=0:raise ValueError('k must be positive')
    return len(set(retrieved_ids[:k]) & set(relevant_ids))/k
