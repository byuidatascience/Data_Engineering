import boto
import numpy as np
import multiprocessing
from time import sleep
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF
from sklearn.datasets import fetch_20newsgroups
from time import time
from bs4 import BeautifulSoup

conn = boto.connect_s3()
bucket = conn.get_bucket('rawtweets100')
keys = bucket.get_all_keys()
corpus = []


def func2(bucket, keys):
    for k in keys:
        #print (k)
        html = k.get_contents_as_string()
        #print (html)
        soup = BeautifulSoup(html)  # parses the html text
        content = soup.findAll(class_='story-body-text story-content')  # finds the main article using HTML tags
        final_content = ''
        for line in content:
            #line = BeautifulSoup(str(line))
            final_content += BeautifulSoup(str(line)).get_text() + ' '
        corpus.append(final_content)
        #print (corpus)
        print('Added one article to corpus')
    return corpus


cpu_count = multiprocessing.cpu_count()
print("This machine has {} cpu's".format(cpu_count))


def some_function(i, cpu_count):
    # sleep(i)
    # print("Job finished. I just slept for {} seconds".format(i))
    iterable = np.ones(cpu_count) * 3
    pool = multiprocessing.Pool(processes=cpu_count)
    outputs = pool.map(some_function, iterable)


def return_topics(corpus):
    n_features, n_topics, n_top_words = 1000, 10, 5
    # Use tf-idf features for NMF.
    print("Extracting tf-idf features for NMF...")
    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
                                       max_features=n_features,
                                       stop_words='english')
    tfidf = tfidf_vectorizer.fit_transform(corpus)
    nmf = NMF(n_components=n_topics, random_state=1,
              alpha=.1, l1_ratio=.5).fit(tfidf)

    print("\nTopics in NMF model:")
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    print_top_words(nmf, tfidf_feature_names, n_top_words)

#n_samples, n_features, n_topics, n_top_words = 2000, 1000, 10, 20

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


return_topics(func2(bucket, keys))
