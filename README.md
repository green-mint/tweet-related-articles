# tweet-related-articles
A browser extension to fetch relevant articles and news about the current tweet being viewed

No matter how hard someone tries, 280 characters can never be enough to convey the detailed intended message. This is especially true for news bits that users on twitter engage with. Those small tweets are not enough to provide complete details and context related to a headline. Instead of just scrolling down from the fear of opening a new tab and not getting the full clear picture, <> simply empowers users to get informed about the context and details without ever having to leave the site.

## Contributors
* Syed Asadullah Kashif
* Muhammad Subhan Abbas
* Muhammad Saad ur Rehman

## Getting Started

## Working
On clicking the <svg of the button> the the tweets are parsed and sent to the Flask RESTful backend running on Heroku. Here improtant keyphrases are extracted from the tweets and quried on Google which return article links and article heads. The article heads are passed through a similarity function to measure how much similar they are to the tweet and score each article. Finally, the article links, the article heads and the article scores are returned to the front-end to be rendered for the user 

## TechStack
* Javascript
* Flask
* Google Custom Search API
* SBERT.net
* NLTK

## Future TODOs
