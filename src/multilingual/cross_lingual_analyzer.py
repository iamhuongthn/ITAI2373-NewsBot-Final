"""Cross-language retrieval; original-language sourcing is required for cultural claims."""
class CrossLingualAnalyzer:
    def __init__(self,search_engine,metadata=None):
        self.search_engine=search_engine
        self.metadata=metadata
    def compare(self,query,top_k=5,language=None):
        indices=None
        if language is not None:
            if self.metadata is None:raise ValueError('Supply original-language article metadata for filtering')
            indices=[i for i,item in enumerate(self.metadata) if item.get('language')==language]
        return self.search_engine.search(query,top_k=top_k,indices=indices)
