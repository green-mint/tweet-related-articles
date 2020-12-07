from rake_nltk import Rake

def extract(text,num_phrases):
    extractor = Rake()
    r.extract_keywords_from_text(text)
    phrases = r.get_ranked_phrases()[:num_phrases]
    return phrases
    

