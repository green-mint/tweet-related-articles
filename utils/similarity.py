from sentence_transformers import SentenceTransformer, util

def similarity(tweet,article_heads):
    model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
    cosine_scores = []
    tweet_embedding = model.encode(tweet, convert_to_tensor=True)
    for i in range(len(article_heads)):
        article_embedding = model.encode(article_heads[i], convert_to_tensor=True)
        cosine_scores.append(float(util.pytorch_cos_sim(tweet_embedding, article_embedding).numpy()))
    return cosine_scores