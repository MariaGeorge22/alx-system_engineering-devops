#!/usr/bin/python3

"""
Queries the Reddit API
and returns the number of subscribers for a given subreddit
"""

import requests

BASE = 'https://www.reddit.com/r/'


def recurse(subreddit, hot_list=[]):
    """function"""
    headers = {'User-Agent': 'my-app/0.0.1'}
    after = ''
    if len(hot_list) > 0:
        after = '?after=' + hot_list[-1].get('name')
    data = requests.get(BASE + str.format("{}/hot.json{}",
                                subreddit, after), headers=header,
                                allow_redirects=False)
    if data.status_code != 200:
        return None
    hot_list += [post.get('data')
            for post in data.json().get('data').get('children')]
    if data.json().get('data').get('after') is None:
        return [post.get('title') for post in hot_list]
    return recurse(subreddit, hot_list)
