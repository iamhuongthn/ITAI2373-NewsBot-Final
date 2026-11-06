from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / 'data' / 'raw' / 'BBC News Train.csv'
MODEL = ROOT / 'data' / 'models' / 'classifier.joblib'
EMBEDDINGS = ROOT / 'data' / 'models' / 'embeddings.npy'
MAX_ARTICLES = 1440
