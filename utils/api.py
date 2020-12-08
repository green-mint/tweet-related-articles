from apiclient.discovery import build
from typing import List
from dotenv import find_dotenv
import os

find_dotenv('../.env')


class GoogleResult():
    def __init__(self, title: str, link: str) -> None:
        self.title = title.strip()
        self.link = link.strip()


def get_google_results(query: str, result_count: int = 5) -> List[GoogleResult]:
    """Returns the GoogleResult of the results received from the keyboard"""

    resource = build("customsearch", 'v1',
                     developerKey=os.environ.get('YOUTUBE_API')).cse()

    results = resource.list(
        q=query, cx=os.environ.get('YOUTUBE_CSX')).execute()

    result_set: List[GoogleResult] = []

    for i in range(result_count):

        title = results['items'][i].get('title', '')
        link = results['items'][i].get('link', '')

        result_set.append(GoogleResult(title, link))

    return result_set
