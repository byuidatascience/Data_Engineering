#!/usr/bin/env python3

import sys
import json
import pandas as pd

from functools import partial
from toolz.dicttoolz import get_in

tweet_str = open('/Users/Alphabum/Downloads/twitterstreamfile.txt','r')


def get_urls(tweet):
    '''return an iterable of urls'''
    base = partial(dict(),tweet)
    base = map(dict(),tweet)
    return map(get_in('url'),base)
    partial(iter(base))
    



for tweet_str in sys.stdin:
<<<<<<< HEAD
     tweet = json.loads(tweet_str)
     expanded_urls = get_urls(tweet)
     assert type(expanded_urls) == map
     for expanded_url in get_urls(tweet):
         print(tweet.get('id'), expanded_url, sep='\t')

print (streamer.read())

get_urls(tweet_str)
=======
    tweet = json.loads(tweet_str)
    expanded_urls = get_urls(tweet)
    assert type(expanded_urls) == map
    for expanded_url in expanded_urls:
        print(tweet.get('id'), expanded_url, sep='\t')
>>>>>>> upstream/master
