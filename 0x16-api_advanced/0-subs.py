#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
  """
  Queries the Reddit API for the number of subscribers of a given subreddit.

  Args:
    subreddit: The name of the subreddit.

  Returns:
    The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
  """

  url = f"https://www.reddit.com/r/{subreddit}/about.json"
  headers = {'User-Agent': 'Ubuntu 20.04'}

  try:
    response = requests.get(url  , headers=headers)
    response.raise_for_status()
    data = response.json()
    return data['data']['subscribers']
  except requests.exceptions.RequestException:
    return 0

