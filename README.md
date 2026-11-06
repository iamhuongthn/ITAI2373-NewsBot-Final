# NewsBot Intelligence System 2.0 - ITAI 2373 Final Project

**Repository:** `ITAI2373-NewsBot-Final`  
**Original midterm:** https://github.com/iamhuongthn/ITAI2373-NewsBot-Midterm  

## Overview

NewsBot 2.0 extends the original midterm's BBC news classification, VADER sentiment and spaCy NER with LDA/NMF topic discovery, sentence-embedding semantic search, pretrained summarization, English/Vietnamese translation, a stateful conversational interface and an optional Flask web application. The original midterm reported 1,490 BBC rows and 1,440 unique articles after deduplication. This package does **not** claim to reproduce the original midterm's 94.44% test accuracy: the new classifier configuration must be measured separately.

## Google Colab (recommended)

## Local setup (Python 3.10-3.12)

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python scripts/setup_data.py
python scripts/train.py
python scripts/evaluate.py
python -m pytest -q
python app.py
```

Open http://127.0.0.1:5000. Run commands from the repository root. On some environments the optional transformer models may be unavailable or require additional memory.

## Structure

- `src/data_processing`: dataset validation and text/feature preprocessing
- `src/analysis`: Naive Bayes classifier, LDA/NMF, VADER sentiment, spaCy NER
- `src/language_models`: pretrained summarization, embeddings, evidence-only enhancement
- `src/multilingual`: language detection, optional en <-> vi translation, cross-language retrieval
- `src/conversation`: deterministic intent classification, contextual follow-ups
- `src/utils`: evaluation, visualizations, JSON export
- `notebooks`: eight executable Colab notebooks (quickstart + seven focused modules)
- `scripts`: data setup, training, evaluation, optional original midterm notebook download
- `app.py`, `templates`, `static`: local Flask dashboard and API
- `tests`: unit and integration tests that avoid downloading heavy transformer models
- `docs`, `reports`, `evaluation`, `demo`: documentation, output directories, evidence

## Data and attribution

`python scripts/setup_data.py` downloads the BBC CSV from the original public midterm repository. The ZIP does not duplicate the 3.3 MB BBC CSV or 7.8 MB original notebook. To download the unchanged original notebook for an archive, run `python scripts/fetch_midterm_notebook.py`. Do not commit datasets or models without checking licenses and file size. The BBC corpus has **no genuine publication dates**; trend methods must not fabricate them. Cultural comparisons require independently sourced original-language news, not merely translated duplicates.

## Evaluation and limitations

`python scripts/evaluate.py` writes actual held-out classification metrics to `evaluation/final_classifier_evaluation.json`. Topic quality, semantic search relevance, summary factuality, translation quality, conversation accuracy and production deployment need additional evaluation. Model probabilities are not calibrated confidence guarantees. Co-occurring entities are not verified relationships. This project is an academic demonstration, not a production-hardened service.

