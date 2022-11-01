'''checks number of subscribers for a given subreddit'''
import requests


def number_of_subscribers(subreddit):
    '''fetches number of subscribers for subreddit'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Http Agent 1.1'})
    res = requests.get(url, headers=headers).json()
    subscribers = res.get('data', {}).get('subscribers', None)
    if subscribers is None:
        return 0
    return subscribers
