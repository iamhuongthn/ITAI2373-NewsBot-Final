from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
class SentimentAnalyzer:
    def __init__(self): self.model=SentimentIntensityAnalyzer()
    def analyze(self,text):
        scores=self.model.polarity_scores(text)
        label='positive' if scores['compound']>=.05 else 'negative' if scores['compound']<=-.05 else 'neutral'
        return {'label':label,'scores':scores}
    def evolution(self,df,date_col='published_at',text_col='text'):
        """Use only genuine timestamps. Missing dates cannot support time trends."""
        if date_col not in df or df[date_col].isna().all():
            return {'available':False,'reason':'No authentic publication dates in supplied articles'}
        valid=df.dropna(subset=[date_col]).copy()
        valid['month']=pd.to_datetime(valid[date_col],utc=True).dt.to_period('M').astype(str)
        valid['compound']=valid[text_col].map(lambda s:self.analyze(s)['scores']['compound'])
        return {'available':True,'monthly_mean':valid.groupby('month')['compound'].mean().round(3).to_dict()}
