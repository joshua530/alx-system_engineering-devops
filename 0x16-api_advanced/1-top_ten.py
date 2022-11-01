#!/usr/bin/python3
'''fetches top ten posts for a given subreddit'''
import requests


def top_ten(subreddit):
    '''fetches top ten posts for a subreddit'''
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Http Agent 1.1'})
    res = requests.get(url, headers=headers).json()
    top_10 = res.get('data', {}).get('children', None)
    if top_10 is None:
        print(None)
    for post in top_10:
        print(post.get('data').get('title'))
