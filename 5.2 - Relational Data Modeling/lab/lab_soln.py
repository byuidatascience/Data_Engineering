'''
Schema w/ 3 tables

TABLE tweets has the following columns:
    tweet_id - bitint - PRIMARY KEY and NOT NULL
    text - character varying
    user_id - bigint
    timestamp_ms - bigint
    created_at - timestamp w/ tz
    lang - character varying
    possibly_sensitive - Boolean

TABLE entities has the following columns:
    tweet_id - bitint - PRIMARY KEY and NOT NULL
    hashtag - character varying - PRIMARY KEY and NOT NULL

TABLE users has the following columns:
    user_id - bigint - PRIMARY KEY and NOT NULL
    screen_name - character varying
    followers_count - bigint
'''

import json
from os.path import expanduser
import psycopg2
from psycopg2 import IntegrityError, InternalError
import sys
import time
import yaml


def get_tweets(tweet):
    '''
    INPUT: dict of tweets
    OUTPUT: list of length 7 w/ the following values:
            tweet_id
            text
            user_id
            timestamp_ms
            created_at
            lang
            possibly_sensitive
    '''
    try:
        tweet_id = tweet['id']
        text = tweet['text']
        user_id = tweet.get('user')
        if user_id:
            user_id = user_id.get('id')
        timestamp_ms = tweet.get('timestamp_ms')  # machine readable timestamp
        created_at = tweet.get('created_at')  # human readable timestamp
        created_at = time.strftime('%Y-%m-%d %H:%M:%S',
                        time.strptime(created_at,'%a %b %d %H:%M:%S +0000 %Y'))
        lang = tweet.get('lang')
        possibly_sensitive = tweet.get('possibly_sensitive')
        return [tweet_id, text, user_id, timestamp_ms, created_at, lang,
                    possibly_sensitive]
    except ValueError:
        pass


def get_users(tweet):
    '''
    INPUT: dict of tweets
    OUTPUT: list of length 3 w/ the following values:
            user_id
            screen_name
            followers_count
    '''
    try:
        users = tweet.get('user')
        if users:
            user_id = users.get('id')
            screen_name = users.get('screen_name')
            followers_count = users.get('followers_count')
        return [user_id, screen_name, followers_count]
    except ValueError:
        pass


def get_entities(tweet):
    '''
    INPUT: dict of tweets
    OUTPUT: generator that yeilds lists w/ the following values:
        tweet_id
        hashtag
    '''
    try:
        if 'entities' in tweet:
            for hashtag in tweet['entities'].get('hashtags', []):
                yield [tweet['id'], hashtag['text']]
    except ValueError:
        pass


def main(credentials, source=sys.stdin):
    '''
    INPUT: None
    OUTPUT: None
        Inserts all tweets into postgres using `get_tweets`
    For more on the errors see:
        http://initd.org/psycopg/docs/module.html#exceptions
    '''
    conn = psycopg2.connect(**credentials)
    cur = conn.cursor()
    total_count = 0

    for tweet_str in source:
        if 'entities' in tweet_str:
            total_count += 1
            tweet = json.loads(tweet_str)
            tr, ur, er = get_tweets(tweet), get_users(tweet), get_entities(tweet)

            try:
                cur.execute("INSERT INTO tweets VALUES (%s,%s,%s,%s,%s,%s,%s)",
                    tr)
                if er:
                    for row in er:
                        cur.execute("INSERT INTO entities VALUES (%s,%s)",
                            row)
                conn.commit()
                cur.execute("INSERT INTO users VALUES (%s,%s,%s)",
                    ur)
                conn.commit()

            except (IntegrityError, InternalError) as e:  # prevents duplicates
                cur.execute("rollback")
                print('Tweet # {}: {}'.format(total_count, tr))

    conn.commit()
    conn.close()
    print('Inserted {} tweets'.format(total_count))

if __name__ == '__main__':
    credentials = yaml.load(open(expanduser('~/.ssh/postgres.yml')))
    main(credentials=credentials['rds'])
