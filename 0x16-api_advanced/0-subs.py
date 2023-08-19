#!/usr/bin/env python3
"""Module containing a function to get number of subscribes"""
import requests


def number_of_subscribers(subreddit):
    """
    Fetch the total number of subscribers from reddit api
    for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    data = requests.get(url, headers={'User-agent': 'daniel etchie'})
    if data.status_code == 200:
        return data.json().get('data').get('subscribers')
    else:
        return 0
