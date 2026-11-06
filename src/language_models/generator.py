class ContentEnhancer:
    """Evidence-only context: key entities and relevant retrieved passages, no invented facts."""
    def enhance(self,text,entities=None,related=None):
        return {'key_entities':(entities or [])[:10],'related_articles':(related or [])[:5],'note':'Context is extracted from supplied documents; not independently fact-checked.'}
