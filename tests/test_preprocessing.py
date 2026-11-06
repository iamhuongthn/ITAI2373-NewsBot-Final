from src.data_processing.text_preprocessor import clean_text
from src.data_processing.data_validator import load_bbc
import pandas as pd
import pytest

def test_clean_text_preserves_negation():
    assert clean_text('  not   good  ')=='not good'

def test_load_bbc_deduplicates(tmp_path):
    path=tmp_path/'bbc.csv'
    pd.DataFrame({'Text':['A valid article','A valid article','Another valid article'],'Category':['tech','tech','sport']}).to_csv(path,index=False)
    assert len(load_bbc(path))==2

def test_missing_columns(tmp_path):
    path=tmp_path/'bad.csv';pd.DataFrame({'wrong':['text']}).to_csv(path,index=False)
    with pytest.raises(ValueError):load_bbc(path)
