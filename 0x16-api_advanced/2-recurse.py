#!/usr/bin/python3
'''
Modue that contains a function recurse that recursively calls
Reeddit Api for titles
'''
import requests


def recurse(subreddit, hot_list=[], next_page=None, count=0):
    '''
    Queries Reddit Api for recursively for titles
    Args:
        subreddit(str) - The name of the subreddit to check
        hot_list - List to append
        next_page - Page to be passed in parameter
        count - Counter
    '''
    user_agent = 'DellServer22.04'
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    # if page specified, pass as parameter
    if next_page:
        url += '?after={}'.format(next_page)
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return None

    data = r.json()['data']
    posts = data['children']
    for post in posts:
        count += 1
        hot_list.append(post['data']['title'])

    next_page = data['after']
    if next_page is not None:
        return recurse(subreddit, hot_list, next_page, count)
    else:
        return hot_list
