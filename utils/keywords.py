from rake_nltk import Rake
from typing import List


def extract(text: str, num_phrases: int = 3) -> List[str]:
    extractor = Rake()
    extractor.extract_keywords_from_text(text)
    phrases = extractor.get_ranked_phrases()[:num_phrases]
    return phrases
