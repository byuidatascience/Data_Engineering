import json
from os.path import expanduser
import psycopg2
from psycopg2 import IntegrityError, InternalError
import sys
import time
import yaml

credentials = yaml.load(open(expanduser('~/.ssh/postgres.yml')))

'''
TABLE tweets has the following columns:
    tweet_id - bitint - PRIMARY KEY and NOT NULL
    text - character varying - PRIMARY KEY and NOT NULL
    user_id - bigint
    timestamp_ms - bigint
    created_at - timestamp w/ tz
    lang - character varying
    possibly_sensitive - Boolean
'''

def get_tweets(tweet_str):
    '''
    INPUT: JSON string of tweets
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
        tweet = json.loads(tweet_str)
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
    row_count, total_count = 0, 0
    for tweet_str in source:
        if '"hashtags": [{' in tweet_str:
            row_count += 1
            row = get_tweets(tweet_str)
            try:
                cur.execute("INSERT INTO tweets VALUES(%s,%s,%s,%s,%s,%s,%s)",
                    row)
                total_count += 1
            except (IntegrityError, InternalError):  # prevents duplicates
                pass
            if row_count > 99:
                conn.commit()
                row_count = 0
    conn.commit()
    conn.close()
    print('Inserted {} tweets'.format(total_count))

if __name__ == '__main__':
    main(credentials=credentials['rds'])
