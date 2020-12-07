from typing import Text
from flask import Flask
from flask_restful import Resource, Api
from keywords.keywords import extract

app = Flask(__name__)
api = Api(app)


class TextToLinks(Resource):

    def get(self: Resource, text: str):
        return {
            "links": extract(text)
        }



api.add_resource(TextToLinks, '/<string:text>')


if __name__ == '__main__':
    app.run(debug=True)
