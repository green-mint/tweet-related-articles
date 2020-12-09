import spacy
from typing import List


def similarity(tweet: str, article_heads: List[str]) -> List[float]:
    """Returns the similarity indices for each of the titles"""

    model = spacy.load('en_core_web_md')
    cosine_scores: List[float] = []
    tweet_embedding = model(tweet)
    for i in range(len(article_heads)):
        article_embedding = model(article_heads[i])
        cosine_scores.append(tweet_embedding.similarity(article_embedding))

    return cosine_scores 
