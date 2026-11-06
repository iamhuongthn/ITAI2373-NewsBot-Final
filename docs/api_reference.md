# API reference

`GET /api/health`: JSON health and dataset availability.

`POST /api/analyze`: JSON `{"text":"...", "summarize":false}`; returns category, estimated probability, sentiment, language and named entities; summary is optional.

`POST /api/query`: JSON `{"query":"..."}`; performs semantic retrieval or contextual follow-up based on per-browser session state.

Python API: `NewsBotEngine(dataset,model_path)`, `.analyze(text)`, `.initialize_topics(n_topics,method)`, `.search(query,top_k)`, `.summarize(text)`, `.translate(text,source,target)`; `TopicModeler(n_topics,method)`, `.fit_transform(documents)`, `.get_topic_words(topic_id)`, `.get_article_topics(text)`.

See module docstrings for implementation details. No guarantee of calibrated classifier probabilities or verified factual accuracy.
