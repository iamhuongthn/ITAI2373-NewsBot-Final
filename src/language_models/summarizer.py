class IntelligentSummarizer:
    def __init__(self,model_name='sshleifer/distilbart-cnn-12-6'):
        from transformers import pipeline
        self.pipe=pipeline('summarization',model=model_name,device=-1)
    def summarize(self,text,max_length=110):
        if len(text.split())<35:return text.strip()
        # Chunk by words to avoid model context overflow.
        words=text.split(); chunks=[' '.join(words[i:i+450]) for i in range(0,min(len(words),1800),450)]
        summaries=[]
        for chunk in chunks:
            out=self.pipe(chunk,max_length=max_length,min_length=20,do_sample=False,truncation=True)
            summaries.append(out[0]['summary_text'])
        return ' '.join(summaries)
