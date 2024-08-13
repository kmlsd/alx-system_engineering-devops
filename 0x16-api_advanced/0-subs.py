#!/usr/bin/python3
""" Queries the Reddit API and returns the
number of subscribers for a given subreddit. 
"""

import requests
headers = {"User-Agent": "Custom"}


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/dev/api/{}/about.json".format(subreddit)
    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 200:
       return request.json().get("data").get("subscribers")

    return 0
