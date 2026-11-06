"""LDA/NMF topic modeling, topic distributions and document clustering."""
import numpy as np
from sklearn.decomposition import LatentDirichletAllocation,NMF
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.cluster import KMeans

class TopicModeler:
    def __init__(self,n_topics=7,method='lda',random_state=42):
        if method not in ('lda','nmf'):raise ValueError('method must be lda or nmf')
        self.method=method;self.n_topics=n_topics;self.random_state=random_state
        vec=CountVectorizer if method=='lda' else TfidfVectorizer
        self.vectorizer=vec(stop_words='english',max_features=6000,min_df=2,max_df=.95)
        self.model=(LatentDirichletAllocation(n_components=n_topics,random_state=random_state,max_iter=15) if method=='lda' else NMF(n_components=n_topics,random_state=random_state,init='nndsvda',max_iter=350))
    def fit_transform(self,documents):
        if len(documents)<self.n_topics:raise ValueError('Need at least n_topics documents')
        matrix=self.vectorizer.fit_transform(documents)
        self.topic_weights=self.model.fit_transform(matrix)
        self.clusterer=KMeans(n_clusters=self.n_topics,random_state=self.random_state,n_init=10).fit(self.topic_weights)
        return self.topic_weights
    def transform(self,documents):return self.model.transform(self.vectorizer.transform(documents))
    def get_topic_words(self,topic_id,n_words=10):
        names=self.vectorizer.get_feature_names_out()
        return [str(names[i]) for i in np.argsort(self.model.components_[topic_id])[-n_words:][::-1]]
    def get_article_topics(self,text):
        scores=self.transform([text])[0]
        return [{'topic':int(i),'weight':round(float(scores[i]),4),'keywords':self.get_topic_words(int(i),5)} for i in np.argsort(scores)[::-1][:3]]
    def visualize_topics(self):
        import plotly.express as px
        counts=np.bincount(self.topic_weights.argmax(axis=1),minlength=self.n_topics)
        return px.bar(x=[f'Topic {i}' for i in range(self.n_topics)],y=counts,labels={'x':'Dominant topic','y':'Articles'},title=f'{self.method.upper()} topic distribution')
    def topic_evolution(self,dates):
        """Return observed monthly topic counts only when genuine dates are supplied."""
        import pandas as pd
        dates=pd.to_datetime(dates,errors='coerce',utc=True)
        if len(dates)!=len(self.topic_weights):raise ValueError('dates must match fitted articles')
        if dates.isna().all():return {'available':False,'reason':'No genuine publication dates'}
        frame=pd.DataFrame({'month':dates.to_period('M').astype(str),'topic':self.topic_weights.argmax(axis=1)})
        return {'available':True,'counts':frame.groupby(['month','topic']).size().reset_index(name='articles').to_dict('records')}
