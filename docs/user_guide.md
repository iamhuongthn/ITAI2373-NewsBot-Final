# NewsBot 2.0 User Guide

1. Follow the README to install and fetch the dataset.
2. Run `python scripts/train.py` to train and save the classifier.
3. Run `python app.py` to open the local Flask dashboard.
4. Paste article text into Analyze to view predicted category, sentiment, detected language and entities.
5. Use Ask NewsBot to search the indexed BBC corpus, then ask for a summary, sentiment, entities, or Vietnamese translation of the selected article.
6. The first semantic search or summarization request may download a pretrained model and take time.

The BBC corpus is historical English news. Queries such as 'this week' cannot return verified recent news without a separately sourced current dated dataset. Model output is not fact-checked news.
