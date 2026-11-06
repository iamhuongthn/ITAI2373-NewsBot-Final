"""Safe JSON export of reproducible analysis results."""
import json
from pathlib import Path

def export_json(data,path):
    destination=Path(path);destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(data,indent=2,ensure_ascii=False,default=str),encoding='utf-8')
    return destination
