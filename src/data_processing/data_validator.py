import pandas as pd
from src.data_processing.text_preprocessor import clean_text

def load_bbc(path):
    """Load Kaggle BBC training CSV; remove exact duplicate article texts."""
    df = pd.read_csv(path)
    required = {'Text', 'Category'}
    if not required.issubset(df.columns):
        raise ValueError(f'Dataset must contain {required}; found {list(df.columns)}')
    df = df.dropna(subset=['Text', 'Category']).copy()
    df['text'] = df['Text'].map(clean_text)
    df['category'] = df['Category'].astype(str).str.lower().str.strip()
    df = df[df['text'].str.len() > 0].drop_duplicates(subset=['text']).reset_index(drop=True)
    df['article_id'] = ['bbc_' + str(i) for i in range(len(df))]
    df['source'] = 'BBC Kaggle historical corpus'
    df['published_at'] = pd.NaT  # Original dataset has no dates.
    return df[['article_id','text','category','source','published_at']]
