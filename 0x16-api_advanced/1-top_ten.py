#!/usr/bin/python3

"""
Queries the Reddit API
and returns the number of subscribers for a given subreddit
"""

import base64
import requests
from urllib.parse import quote

BASE = 'https://www.reddit.com/r/'
CLIENT_ID = "gjV8WEVc3awcbN00hZLVpdD6gbo3_A"


def top_ten(subreddit):
    """function"""
    headers = {
        'User-Agent': 'my-app/0.0.1/220942',
        'Authorization':
        "Basic " +
        base64.b64encode((quote(CLIENT_ID) + ":").encode()).decode()}
    data = requests.get(BASE + str.format("{}/hot.json?limit=10",
                                    subreddit), headers=headers,
                                    allow_redirects=False)
    if data.status_code != 200:
        print(None)
        return
    posts = data.json().get('data').get('children')
    for post in posts:
        print(post.get('data').get('title').encode('utf-8'))
