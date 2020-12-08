from typing import Dict, Text, List
from flask import Flask
from flask_restful import Resource, Api
from utils.keywords import extract
from utils.api import get_google_results

app = Flask(__name__)
api = Api(app)


class TextToLinks(Resource):

    def get(self: Resource, text: str):
        results: List[Dict[str, str]] = []

        phrases = extract(text)

        query = ""
        for phrase in phrases:
            query += phrase

        for result in get_google_results(query):
            results.append({
                'title': result.title,
                'link': result.link
            })

        return results


api.add_resource(TextToLinks, '/<string:text>')


if __name__ == '__main__':
    app.run(debug=True)
