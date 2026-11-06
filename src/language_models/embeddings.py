import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
class SemanticSearchEngine:
    def __init__(self,model_name='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'):
        from sentence_transformers import SentenceTransformer
        self.model=SentenceTransformer(model_name)
    def index(self,articles):
        self.articles=list(articles)
        self.embeddings=self.model.encode(self.articles,batch_size=32,show_progress_bar=True,normalize_embeddings=True)
    def search(self,query,top_k=5,indices=None):
        if not hasattr(self,'embeddings'):raise RuntimeError('Call index() first')
        indices=list(range(len(self.articles))) if indices is None else list(indices)
        if not indices:return []
        q=self.model.encode([query],normalize_embeddings=True)
        scores=cosine_similarity(q,self.embeddings[indices])[0]
        order=np.argsort(scores)[::-1][:top_k]
        return [{'index':int(indices[j]),'score':float(scores[j]),'text':self.articles[indices[j]][:500]} for j in order]
