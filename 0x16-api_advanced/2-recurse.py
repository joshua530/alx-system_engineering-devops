#!/usr/bin/python3
'''returns a list containing the titles of all hot articles
for a given subreddit'''
import requests


def recurse(subreddit, hot_list=[], after=''):
    '''returns a list containing the titles of all hot articles
    for a given subreddit'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after != '':
        url += '?after={}'.format(after)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Http Agent 1.1'})
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return None
    res = res.json()
    articles = res.get('data', {}).get('children', None)
    after = res.get('data').get('after')
    if after is None:
        return
    for post in articles:
        titles = [title for title in post.get('data').get('title')]
    hot_list += titles
    recurse(subreddit, hot_list, after)
    return hot_list
