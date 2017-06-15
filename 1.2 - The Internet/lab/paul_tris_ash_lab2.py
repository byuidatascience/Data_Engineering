#!/usr/bin/env python

#http://tripaul-bucket.s3-website-us-west-1.amazonaws.com/   This is the link to my site.


import os
import yaml
from twitter import Twitter, OAuth
import pprint
import pandas as pd
import time
import boto
import matplotlib.pyplot as plt


def connect_twitter(config_filepath='api_cred.yml'):
    ''' connect to twitter, and return twitter connection
        INPUT: yaml config filepath (optional)
        OUTPUT: Twitter object
    '''

    credentials = yaml.load(open(os.path.expanduser(config_filepath)))
    credentials = credentials['twitter']
    token = credentials.get('token')
    token_secret = credentials.get('token_secret')
    consumer_key = credentials.get('consumer_key')
    consumer_secret = credentials.get('consumer_secret')

    t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))
    return t


def upload_page(page, timestamp):
    '''create a couple of strings with our very minimal web content
    INPUT:
        - page: string formated html page content
        - timestamp: last update date of the page
    OUTPUT: URL of the html page from aws
    '''

    top10_html = """
    <html>
      <head><title>My S3 Webpage</title></head>
      <body><h2>Top 10 twitter trends in San Francisco</h2>{page}</body>
      <img src="bar.png" />
      <footer>
        <p>Last Update: {timestamp}</p>
      </footer>
    </html>""".format(page=page, timestamp=timestamp)

    # create a connection to S3
    conn = boto.connect_s3()
    # create a bucket and make it publicly readable
    mybucket = conn.get_bucket('tripaul-bucket')

    # upload our HTML pages and make sure they are publicly readable
    # also make sure Content-Type is set to text/html
    top10 = mybucket.new_key('top10.html')
    top10.content_type = 'text/html'
    top10.set_contents_from_string(top10_html, policy='public-read')

    # upload bar plot (hard coded as "bar.png")
    bar_plot = mybucket.new_key('bar.png')
    bar_plot.content_type = 'image/png'
    bar_plot.set_contents_from_filename('bar.png', policy='public-read')

    # now set the website configuration for our bucket
    mybucket.configure_website('top10.html')

    time.sleep(5)

    # now get the website configuration, just to check it
    # print(mybucket.get_website_configuration())
    #return top10.generate_url(expires_in=300)


def prepare_page(t):
    '''prepare web page using twitter connection object t
    INPUT: twitter connection object
    OUTPUT: string formatted html page content, timestamp of validity
    '''

    # 2487956 is san francisco

    data = t.trends.place(_id='2487956')[0]
    timestamp = data['as_of']
    topics = data['trends']
    # print(type(topics))
    # print(len(topics[0]))
    topics = sorted(topics,
                    key=lambda topic: topic['tweet_volume']
                    if topic['tweet_volume'] is not None else 0,
                    reverse=True)
    # pprint.pprint(topics[:10])
    df = pd.DataFrame(topics[:10])
    df.index = df.index + 1
    plot = df[['name', 'tweet_volume']].set_index('name').plot(kind='barh')
    plt.xlabel("tweet_volume")
    plt.ylabel("topic")
    fig = plot.get_figure()
    fig.savefig("bar.png")
    page = df.to_html()
    # print(page)
    return page, timestamp

t = connect_twitter()
page, timestamp = prepare_page(t)
url = upload_page(page, timestamp)
print(url)
