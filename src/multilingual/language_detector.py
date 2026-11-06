from langdetect import detect, DetectorFactory
DetectorFactory.seed=42
class LanguageDetector:
    def detect(self,text):
        if not text or len(text.strip())<15:return 'unknown'
        try:return detect(text)
        except Exception:return 'unknown'
