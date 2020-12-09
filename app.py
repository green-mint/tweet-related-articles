from typing import Dict, List, Any
import os

from flask import Flask, request
from flask_restful import Resource, Api, output_json

from utils.keywords import extract
from utils.api import get_google_results
from utils.similarity import similarity
from utils.helper import get_string_from_list

app = Flask(__name__)
api = Api(app)


class TextToLinks(Resource):

    def get(self: Resource):

        text = request.args.get('text', "").strip()
        if not text:
            return {"Error": "No text was provided"}

        # Getting keywords from the text given
        phrases = extract(text)

        query = get_string_from_list(phrases)

        results: List[Dict[str, Any]] = []
        titles: List[str] = []

        # Creating Dicts from the Google's search result.
        for result in get_google_results(query):
            titles.append(result.title)
            results.append({
                'title': result.title,
                'link': result.link,
                'similarity': -1.0
            })

        # Generating a similarilty index from the titles generated
        similarity_indices = similarity(text, titles)

        # for i in range(len(results)):
        #     results[i]['similarity'] = similarity_indices[i]

        return results


# Adding the '/' path for endpoint
api.add_resource(TextToLinks, '/')


if __name__ == '__main__':
    app.run()
