"""Run measurable evaluation on a real downloaded dataset and save results."""
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from config.settings import DATASET
from src.data_processing.data_validator import load_bbc
from src.analysis.classifier import NewsClassifier
from src.utils.export import export_json

def main():
    if not DATASET.exists():raise SystemExit('First run: python scripts/setup_data.py')
    df=load_bbc(DATASET)
    metrics=NewsClassifier().train(df)
    path=export_json({'dataset_rows':len(df),'classifier':metrics,'note':'Measured in current runtime; other modules need their own evaluations.'},'evaluation/final_classifier_evaluation.json')
    print('Saved',path)
if __name__=='__main__':main()
