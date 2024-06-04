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


def number_of_subscribers(subreddit):
    """function"""
    headers = {
        'User-Agent': 'my-app/0.0.1/220942',
        'Authorization':
        "Basic " +
        base64.b64encode((quote(CLIENT_ID) + ":").encode()).decode()}
    data = requests.get(BASE + str.format("{}/about.json",
                        subreddit), headers=headers,
                        allow_redirects=False)
    if data.status_code != 200:
        return 0
    return data.json().get('data').get('subscribers')
