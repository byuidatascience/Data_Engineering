#!/usr/bin/env python3

import requests
import sys
from functools import partial
from toolz.dicttoolz import get_in
import os
import yaml
from twitter import *
import boto3
import json
import time
import queue
from threading import Thread

# Note that these sites might have ways to prevent you from webscraping. One common method is rate limiting. Try using time.sleep() to limits your calls per second

# Tools like Tor and its Python client allow you to mask the origin of your request by daisy chaining it across a network of nodes.

# A .py file with functions to pull twitter data, pull urls from tweets, download articles using GET requests, and placing those articles in s3

# Documentation of the time difference between using threading and not using threading


# start = time.time()

# user_list = ['nytimes', 'BBCWorld', 'OccupyDemocrats', 'AddInfoOrg', 'FoxNews', 'BrietbartNews']

class Threadr(object):
    def __init__(self):
        # Put bucket into here.
        # for name in file name... file_name is list, name is whats in list, name goes into, new.
        # self.user_list = user_list
        #for name in filename:  <-- Chase
        self.user_list = None


    def url(self, link):  # This is the function that gets the actual HTML information from the website.
        #for name in filename:
        r = requests.get(link)
        data = r.text
        # file = new_key(name) #name is the list of url's, which eventually will be your urls
        #file.set_as a string(data,policy =)
        return data

    def get_urls(self, tweet):
        '''return an iterable of urls'''
        return list(map(partial(get_in, ['expanded_url']),
               get_in(['entities', 'urls'], tweet, [])))

    def connect_twitter(self, config_filepath='/vagrant/.ssh/api_cred.yml'):
        credentials1 = yaml.load(open(config_filepath))
        credentials = credentials1['twitter']
        token = credentials.get('token')
        token_secret = credentials.get('token_secret')
        consumer_key = credentials.get('consumer_key')
        consumer_secret = credentials.get('consumer_secret')
        t = TwitterStream(auth=OAuth(token, token_secret, consumer_key, consumer_secret))
        return t
	


    #def grab_data_from_queue(self):
        #while not q.empty(): # check that the queue isn't empty
            #url = q.get() # get the item from the queue
            #r  = requests.get(url) # request the url
            ## ADD YOUR CODE HERE
            #q.task_done() # specify that you are done with the item



    def put_rec(self, account):
        t = self.connect_twitter()
        fire = boto3.client('firehose', region_name = 'us-east-1')
        iterator = t.statuses.filter(follow=account)   #This is where you put the name of the news site, or any other twitter user name
       
        for tweet in iterator:
          if 'urls": [{' in json.dumps(tweet):
            for actual_url in self.get_urls(json.loads(json.dumps(tweet))):
                if actual_url == None:
                  continue
                else:
                  html_data = self.url(link=actual_url)
                  fire.put_record(DeliveryStreamName = 'TwitterNewsStream', Record = {"Data":html_data + "\n"})


    def threads(self):
        t1 = Thread(target=self.put_rec(account='807095'))
        t2 = Thread(target=self.put_rec(account='878284831'))
        t3 = Thread(target=self.put_rec(account='742143'))
        t4 = Thread(target=self.put_rec(account='188014427'))
        t5 = Thread(target=self.put_rec(account='1367531'))
        t6 = Thread(target=self.put_rec(account='799004321702694917'))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()

html_pull = Threadr()


html_pull.threads()




    # specify sitemap to get all site links

    # url_list = ['http://www.nytimes.com']  ## USE YOUR URLS HERE

    # create the queue instance and add urls to the queue
    #  q = queue.LifoQueue()
    # [q.put(url) for url in url_list]

    # define how the URL transformations


    # create and start threads
    # for i in range(12):  # aka the number of threads
        #t1 = Thread(target=grab_data_from_queue)  # target is the above function
        #t1.start()  # start the thread

    # q.join()

    # print('This code took {} seconds'.format(time.time() - start))
