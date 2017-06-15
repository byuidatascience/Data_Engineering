#from flask import Flask
import os
import yaml
from twitter import Twitter, OAuth
import pandas as pd
import time
import matplotlib
# matplotlib is set to recognize environment as MacOS by default, must be
# told not to with Agg, otherwise matplotlib will not work....
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#app = Flask(__name__)

# python3 -m flask run --host=0.0.0.0 <---- Command that initiates flask
# to run the main() function from within @app.route('/')


#@app.route('/')
def main():
    t = connect_twitter()
    page, timestamp = prepare_page(t)
    html_code = upload_page(page, timestamp)
    return html_code

# Originally api_cred.yml file located in local directory, now located in VM.


def connect_twitter(config_filepath='/home/ubuntu/api_cred.yml'):
    credentials = yaml.load(open(os.path.expanduser(config_filepath)))
    credentials = credentials['twitter']
    token = credentials.get('token')
    token_secret = credentials.get('token_secret')
    consumer_key = credentials.get('consumer_key')
    consumer_secret = credentials.get('consumer_secret')
    t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))
    return t


def prepare_page(t):
    data = t.trends.place(_id='2487956')[0]
    timestamp = data['as_of']
    topics = data['trends']
    topics = sorted(topics,
                    key=lambda topic: topic['tweet_volume']
                    if topic['tweet_volume'] is not None else 0,
                    reverse=True)
    df = pd.DataFrame(topics[:10])
    df.index = df.index + 1
    plt1 = df[['name', 'tweet_volume']].set_index('name').plot(kind='barh')
    plt.xlabel("tweet_volume")
    plt.ylabel("topic")
    plt.tight_layout
    fig = plt1.get_figure()
    plt.subplots_adjust(left=0.30)
    fig.savefig("static/bar.png", bbox_inches='tight')
    # File must be saved into a directory named Static because Flask
    # searches only in this directory for static files.
    # Otherwise image will not be found.
    page = df.to_html()
    return page, timestamp


def upload_page(page, timestamp):
    top10_html = """
       <html>
         <head><title>My S3 Webpage</title></head>
          <body><h2>Top 10 twitter trends in San Francisco</h2>{page}</body>
          <img src="static/bar.png" width="700"/>
      <footer>
        <p>Last Update: {timestamp}</p>
      </footer>
      </html>""".format(page=page, timestamp=timestamp)
    return top10_html

#app.run(host="0.0.0.0", port=80)
