from googleapi import google
from typing import List


class GoogleResult():
    def __init__(self, title: str, link: str) -> None:
        self.title = title.strip()
        self.link = link.strip()


def get_google_results(query: str, result_count: int = 5) -> List[GoogleResult]:
    """Returns the GoogleResult of the results received from the keyboard"""

    results = google.search(query, result_count)

    result_set: List[GoogleResult] = []

    for result in results:
        full_title = result.name

        title = full_title[:full_title.rfind("www")]
        link = result.link

        result_set.append(GoogleResult(title, link))

    return result_set[:result_count]
