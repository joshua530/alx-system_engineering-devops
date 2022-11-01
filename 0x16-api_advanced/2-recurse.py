#!/usr/bin/python3
'''returns a list containing the titles of all hot articles
for a given subreddit'''
import requests


def recurse(subreddit, hot_list=[], after=''):
    '''returns a list containing the titles of all hot articles
    for a given subreddit'''
    # get items on current page and store in list
    # if there are no items, return empty list
    # else items = current + recurse(items for next page)
    # return items
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Http Agent 1.1'})
    res = requests.get(url, headers=headers).json()
    top_10 = res.get('data', {}).get('children', None)
    after = res.get('data').get('after')
    if top_10 is None or after is None:
        return
    for post in top_10:
        titles = [title for title in post.get('data').get('title')]
    hot_list += titles
    recurse(subreddit, hot_list, after)
    return hot_list
