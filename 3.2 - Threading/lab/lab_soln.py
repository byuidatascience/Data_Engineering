# -*- coding: utf-8 -*-

import requests
import time
import queue
from threading import Thread
from functools import partial
from toolz.dicttoolz import get_in
import twitter
import yaml
import os
import boto

def get_urls(tweet):
    '''return an iterable of urls'''
    return map(partial(get_in, ['expanded_url']),
               get_in(['entities', 'urls'], tweet, []))


def get_tweets(t_handles):
    '''
    INPUT: list of twitter handles to scrape
    OUTPUT: list of URLS
    '''
    credentials = yaml.load(open(os.path.expanduser(
        '~/.ssh/twitter_api_cred.yml')))
    t = twitter.Twitter(auth=twitter.OAuth(**credentials['twitter']))

    url_list = []
    for user in t_handles:
        tweets = t.statuses.user_timeline(screen_name=user, count=200)
        for tweet in tweets:
            url_list.extend(get_urls(tweet))
    return url_list


def grab_data_from_queue(verbose = False):
    '''
    INPUT: None
    OUTPUT: None
    '''
    while not q.empty():  # check that the queue isn't empty
        url = q.get()  # get the item from the queue
        r = requests.get(url)  # request the url

        k = boto.s3.key.Key(bucket)
        k.key = 'cleaned/' + ''.join(filter(lambda a: a != '/', url))
        k.set_contents_from_string(r.content)
        if verbose:
            print(r.status_code, r.url)
            print('Uploaded {}'.format(k.key))

        q.task_done()  # specify that you are done with the item


if __name__ == '__main__':
    start = time.time()
    t_handles = ['NYTimes', 'BBCWorld',
            'OccupyDemocrats ‏', 'AddInfoOrg',
            'FoxNews', 'BrietbartNews',
            'NewYorker', 'TheAtlantic',
            'YahooNews', 'ABC']
    url_list = get_tweets(t_handles)

    # create the queue instance and add urls to the queue
    q = queue.LifoQueue()
    [q.put(url) for url in url_list]

    # establish s3 connection
    conn = boto.connect_s3()
    bucket = conn.get_bucket('sanbox-bucket')

    for i in range(12):  # aka the number of threads
        t1 = Thread(target = grab_data_from_queue)  # target is the above func
        t1.start()  # start the thread

    q.join()

    print('This code took {} seconds for {} websites'.format(time.time()-start, len(url_list)))
