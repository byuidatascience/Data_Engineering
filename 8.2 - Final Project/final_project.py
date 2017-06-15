#!/usr/bin/python

from indeed import IndeedClient
import time
import yaml
import boto
from boto.s3.key import Key
import json
import urllib.request as request
from fake_useragent import UserAgent
import requests
import socks
import socket
from functools import partial
import numpy as np
from bs4 import BeautifulSoup
from multiprocessing import Pool, cpu_count
from functools import partial

# shhh.... i won't tell anyone if you don't.
socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
socket.socket = socks.socksocket

# import numpy as np
# from bs4 import BeautifulSoup
# from multiprocessing import Pool, cpu_count
from functools import partial


# /usr/local/Cellar/tor/0.2.9.10/bin/tor <--- this is where tor is located.


class Threadr(object):
    def __init__(self, keyword, location):
        self.conn = boto.connect_s3()  # Connecting to S3
        self.bucket = self.conn.get_bucket('bucketofindeeds')  # Accessing the correct bucket
        self.json_up = Key(self.bucket)  # Make sure to name it.
        self.content_up = Key(self.bucket)  # Make sure to name it.
        self.keyword = keyword
        self.location = location
        print('init done')

    def connect_indeed(self, config_filepath='indeed_cred.yml'):  # Store in .ssh
        # yamload = yaml.load(open(config_filepath))
        # credentials = yamload['indeed']
        # pub_num = credentials.get('publisher_num')
        self.c = IndeedClient(publisher='4353162753214099')
        print('connect_indeed done')

    def parameters(self, keyword, location):  # Make sure to try using multiple keywords
        ua = UserAgent(fallback='Your favorite Browser')
        self.params = {
            'q': str(keyword),
            'l': str(location),
            'userip': requests.get("http://icanhazip.com").text,
            'useragent': ua.random
        }
        print('parameters done')

    def job_search(self):
        self.response = self.c.search(**self.params)
        # This will return a json file.
        print(len(self.response['results']),'jobs returned.')

    def send_json(self):
        self.json_up.key = 'indeed_jsons/test'
        self.json_up.set_contents_from_string(str(self.response) + '\n')
        print('Its Working.')



    def mine_that(self):
        self.connect_indeed()
        self.parameters(self.keyword, self.location)
        self.job_search()
        self.send_json()


mine_it = Threadr(("data", "scientist"), "san francisco, ca")
if __name__ == "__main__":
    mine_it.mine_that()
