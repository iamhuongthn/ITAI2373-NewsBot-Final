"""Optional: fetch the exact original midterm notebook for side-by-side comparison."""
import urllib.request
from pathlib import Path
URL='https://raw.githubusercontent.com/iamhuongthn/ITAI2373-NewsBot-Midterm/master/notebooks/Midterm_NewsBot_Intelligence_System.ipynb'
target=Path(__file__).resolve().parents[1]/'notebooks'/'Midterm_NewsBot_Intelligence_System.ipynb'
if not target.exists():
    print('Downloading original midterm notebook (about 8 MB)...')
    urllib.request.urlretrieve(URL,target)
print('Available:',target)
