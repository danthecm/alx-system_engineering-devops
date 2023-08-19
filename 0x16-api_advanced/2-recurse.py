#!/usr/bin/python3
""" Subreddit recurse."""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    Get the Number of subcribers in a subreddit.

    Args:
        subreddit (str): the subreddit to get the info of
    """
    if after is None:
        return
    url = "https://www.reddit.com/r/{:s}/hot.json?after={:s}&limit=100".format(
        subreddit, after)
    response = requests.get(url,
                            allow_redirects=False,
                            headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        data = response.json()
        after = data.get('data').get('after')
        hot_list.extend(data.get('data').get('children'))
        recurse(subreddit, hot_list, after)
    else:
        return None
    return hot_list
