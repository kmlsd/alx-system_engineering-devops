
#!/usr/bin/python3
""" Queries the Reddit API and returns the
number of subscribers for a given subreddit. """

import requests
headers = {"User-Agent": "ubuntu"}


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    request = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")

