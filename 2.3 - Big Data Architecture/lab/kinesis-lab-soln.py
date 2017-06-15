#!/usr/bin/env python3

import json
import os
import sys

import boto3
import yaml

from twitter import OAuth, TwitterStream


def initialize(credentials):
    oauth = OAuth(**credentials['twitter'])
    twitter_stream = TwitterStream(auth=oauth)
    kinesis = boto3.client('firehose',
                           region_name='us-east-1',
                           **credentials['aws'])
    return twitter_stream, kinesis


def stream_tweets(twitter_stream, client, stream_name):
    # Get a sample of the public data following through Twitter
    for tweet in twitter_stream.statuses.sample():
        client.put_record(
            DeliveryStreamName=stream_name,
            Record={'Data': json.dumps(tweet) + '\n'})


if __name__ == '__main__':
    credentials = yaml.load(open(os.path.expanduser('~/api_cred.yml')))
    twitter_stream, kinesis = initialize(credentials)
    while True:
        stream_tweets(twitter_stream, kinesis, 'kinesis-lab-23')
        sys.stdout.write('.')
