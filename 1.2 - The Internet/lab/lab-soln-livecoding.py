#!usr/bin/env python

import boto
import os
import pandas as pd
import ssl
import twitter
import yaml


def main():
    '''
    This pulls top trends from an area
    1. Import credentals
    2. connect to twitter API
    3. Pull top trends
    4. Save as html
    5. Push to s3
    '''
    credentials = yaml.load(open(os.path.expanduser('~/.ssh/twitter_api_cred.yml')))

    t = twitter.Twitter(auth=twitter.OAuth(**credentials['twitter']))

    df = pd.DataFrame(t.trends.place(_id = 1)[0]['trends']).sort_values('tweet_volume', ascending=False)

    df.iloc[:10,:].to_html('trends.html')

    conn = boto.connect_s3()

    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    bucket = conn.get_bucket('superawesomedataproject.com')
    file = bucket.new_key('lab_demo.html')
    file.set_contents_from_filename('trends.html', policy='public-read')


if __name__ == '__main__':
    main()
