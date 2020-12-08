from typing import List


def get_string_from_list(words: List[str]) -> str:
    """Get the single string from a list of strings"""
    query = ""
    for word in words:
        query += word

    return query
