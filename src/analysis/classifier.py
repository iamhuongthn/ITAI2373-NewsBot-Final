from pathlib import Path
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report

class NewsClassifier:
    def __init__(self, model=None):
        self.model = model or Pipeline([('tfidf', TfidfVectorizer(stop_words='english', max_features=12000, ngram_range=(1,2))), ('classifier', MultinomialNB(alpha=0.1))])
    def train(self, df):
        X_train,X_test,y_train,y_test=train_test_split(df.text,df.category,test_size=.2,random_state=42,stratify=df.category)
        self.model.fit(X_train,y_train)
        y_pred=self.model.predict(X_test)
        return {'accuracy':float(accuracy_score(y_test,y_pred)), 'macro_f1':float(f1_score(y_test,y_pred,average='macro')), 'classification_report':classification_report(y_test,y_pred,output_dict=True)}
    def predict(self,text):
        label=str(self.model.predict([text])[0])
        probs=self.model.predict_proba([text])[0]
        ranks=sorted(zip(self.model.classes_,probs),key=lambda x:-x[1])
        return {'category':label,'estimated_probability':round(float(ranks[0][1]),4),'alternatives':[{'category':str(c),'estimated_probability':round(float(v),4)} for c,v in ranks[1:3]],'note':'Probabilities are not calibrated confidence guarantees.'}
    def save(self,path):
        Path(path).parent.mkdir(parents=True,exist_ok=True);joblib.dump(self.model,path)
    @classmethod
    def load(cls,path):
        return cls(joblib.load(path))
