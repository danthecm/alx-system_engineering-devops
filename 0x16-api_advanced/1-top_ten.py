#!/usr/bin/python3
"""Module that contains a function that returns top ten hostest subreddits"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the 10 hottest posts on a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    data = requests.get(url, headers={'User-agent': 'Oluwabunmi Olabode'},
                        allow_redirects=False)
    if data.status_code == 200:
        post_list = data.json().get('data').get('children')
        count = 0
        for post in post_list:
            if count == 10:
                break
            print(post.get("data").get("title"))
            count = count + 1
    else:
        print("None")
