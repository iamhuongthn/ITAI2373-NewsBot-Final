class Translator:
    """Optional on-demand English/Vietnamese translation using Helsinki-NLP models."""
    MODEL_IDS={('en','vi'):'Helsinki-NLP/opus-mt-en-vi',('vi','en'):'Helsinki-NLP/opus-mt-vi-en'}
    def __init__(self):self.pipes={}
    def translate(self,text,source='en',target='vi'):
        if source==target:return text
        key=(source,target)
        if key not in self.MODEL_IDS:raise ValueError('This demonstration supports en↔vi translation only')
        if key not in self.pipes:
            from transformers import pipeline
            self.pipes[key]=pipeline('translation',model=self.MODEL_IDS[key],device=-1)
        return self.pipes[key](text[:3000],max_length=512,truncation=True)[0]['translation_text']
