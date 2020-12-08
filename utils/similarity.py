from sentence_transformers import SentenceTransformer, util
from typing import List


def similarity(tweet: str, article_heads: List[str]) -> List[float]:
    """Returns the similarity indices for each of the titles"""

    model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
    cosine_scores: List[float] = []
    tweet_embedding = model.encode(tweet, convert_to_tensor=True)

    for i in range(len(article_heads)):
        article_embedding = model.encode(
            article_heads[i], convert_to_tensor=True)
        cosine_scores.append(float(util.pytorch_cos_sim(
            tweet_embedding, article_embedding).numpy()))

    return cosine_scores
