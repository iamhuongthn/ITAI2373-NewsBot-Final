# NewsBot data

The midterm used the BBC News Train.csv dataset from Kaggle (1,490 original rows, 1,440 unique article texts after deduplication). Its original data has no genuine publication dates or independent article headlines. Never present inferred dates or generated title proxies as authentic metadata.

Run `python scripts/setup_data.py` to fetch the publicly available CSV from the original midterm repository into `data/raw/`. The dataset is not duplicated inside this ZIP. Review the original Kaggle dataset's redistribution terms before publishing it elsewhere.

`data/multilingual/` contains a template for independently sourced English/Vietnamese articles; populate it with licensed text and genuine source URLs, language and publication dates. No cultural-comparison results should be claimed until original-language sources are collected and reviewed.
