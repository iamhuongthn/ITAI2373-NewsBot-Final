import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Download original midterm BBC CSV from the user's public GitHub repository."""
from pathlib import Path
import urllib.request
from config.settings import DATASET
URL='https://raw.githubusercontent.com/iamhuongthn/ITAI2373-NewsBot-Midterm/master/data/BBC%20News%20Train.csv'
def main():
    DATASET.parent.mkdir(parents=True,exist_ok=True)
    if DATASET.exists():print('Dataset already present:',DATASET);return
    print('Downloading original BBC dataset from midterm repository...')
    urllib.request.urlretrieve(URL,DATASET)
    print('Saved',DATASET,DATASET.stat().st_size,'bytes')
if __name__=='__main__':main()
