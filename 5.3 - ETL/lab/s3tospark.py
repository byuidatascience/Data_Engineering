%pyspark

%pyspark
rdd = sc.textFile("s3a://final_twitter").cache()

%pyspark
rdd.count()

%pyspark
import json
import psycopg2
from psycopg2 import IntegrityError, InternalError
import time

%pyspark
def get_tweets(tweet):
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

%pyspark
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

%pyspark

def get_entities(tweet):
    try:
        if 'entities' in tweet:
            for hashtag in tweet['entities'].get('hashtags', []):
                yield [tweet['id'], hashtag['text']]
    except ValueError:
        pass
%pyspark

def notmain(source):
    conn = psycopg2.connect(**{'dbname': 'postgres', 'host': 'postgres.ckwu3hwuvo1cu.us-east-1.rds.amazonaws.com', 'password': 'censored', 'user': 'ubuntu'})

    cur = conn.cursor()

    for tweet_str in source:
        if 'entities' in tweet_str:
            tweet = json.loads(tweet_str)
            tr, ur, er = get_tweets(tweet), get_users(tweet), get_entities(tweet)

            try:
                cur.execute("INSERT INTO tweets(tweet_id, text, user_id, timestamp_ms, created_at, lang, possibly_sensitive) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                    tr)
                if er:
                    for row in er:
                        cur.execute("INSERT INTO entities1 VALUES (%s,%s)",
                            row)
                conn.commit()
                cur.execute("INSERT INTO users1 VALUES (%s,%s,%s)",
                    ur)
                conn.commit()

            except (IntegrityError, InternalError) as e:  # prevents duplicates
                cur.execute("rollback")

    conn.commit()
    conn.close()

%pyspark
rdd.foreachPartition(notmain)