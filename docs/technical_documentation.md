# NewsBot 2.0 Technical Documentation (living draft)

## Source and architecture
This implementation extends the documented BBC News midterm project. It uses a TF-IDF + Multinomial Naive Bayes baseline; LDA/NMF topic models; VADER sentiment; spaCy NER; lazy transformer summarization; multilingual sentence embeddings; optional English/Vietnamese translation; deterministic conversation state; Flask API.

## Data integrity
The original Kaggle BBC training CSV contains 1,490 rows, with 1,440 unique articles after exact-text deduplication as reported in the midterm. The BBC data does not contain genuine publication timestamps. Topic/sentiment evolution must be disabled until a separately sourced dated corpus is added.

## Reproduction
See README for local/Colab setup. `scripts/train.py` saves a baseline classifier; `scripts/evaluate.py` generates held-out classification metrics; `pytest -q` checks critical functions. Transformer models are downloaded on first use and can be slow.

## Limits and open requirements
This is a runnable development project, not a production deployment. Topic coherence, search relevance, translation quality, summaries, cultural comparisons and full multi-turn accuracy require independent evaluations. Security hardening, deployed frontend, final report figures and team contributions remain to be completed.
