 Multiprocessing
-------------------------

#### By the end of this assignment you should have:

- Used the `bs4` (BeautifulSoup) library to parse html
- Performed Non-negative Matrix Factorization (NMF) on a studied dataset to pull out latent features
- Performed NMF using the `multiprocessing` module on the data your class webscraped
- Compared the performance of using a singular process with using multiple processes

Introduction
----

In unsupervised learning problems, Non-negative Matrix Factorization (NMF) is a technique that, amongst its other benefits, allows us to pull latent features from a given dataset.  In the realm of Natural Language Processing (NLP), this can mean topics within a corpus (or collection) of documents (newspaper articles in our case).

In this assignment we will look for these latent features using one process and using multiple processes in order to see what themes come up in different news sites.  Recall that webscraping is an **I/O bound problem**.  By contrast, this task is **a CPU bound problem** in that our biggest limitation is the processing of our data rather than the transmission of data over a network.  We can speed up this process using multiprocessing.

We will begin by using the `bs4` (or BeautifulSoup) module to help us parse out the text from the sites we scraped.  We will then feed the results into NMF.

Step 1: Parsing Our Data using BeautifulSoup
---------

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is the python library for pulling data out of HTML and XML files.  Used with the `requests` library we saw in the last lab, these comprise the de facto python libraries for webscraping.  Here's a quick look at how we'd pull the articles out of the jumbled mess that is HTML:

        from bs4 import BeautifulSoup
        import requests

        url = 'https://www.nytimes.com/2017/03/29/technology/samsung-after-combustible-galaxy-note-7-unveils-new-smartphone.html'
        r = requests.get(url)
        soup = BeautifulSoup(r.content) # parses the html text
        content = soup.findAll(class_ = 'story-body-text story-content') # finds the main article using HTML tags

        for line in content:
            line = BeautifulSoup(str(line))
            print(line.get_text()) # prints the content of the article without html tags

In this case, New York Times keep the body of the story under the tag 'story-body-text story-content'.  You would know this by using Chrome developer tools under `View -> Developer -> Developer Tools`.

Use this example to understand the specific characteristics of the articles you scraped.  Be sure that at least one pair of students is working on a given news source.  Parse the articles to prepare them for downstream analysis by creating a list of strings where each string is a separate article.

Step 2: NMF on a Studied Dataset
---------

This exercise will give you some intuition into NMF.  You'll learn more about this technique in other coursework at Galvanize.  Suffice it to say that we start by turning a document into an array of values where each value in the array is a count of a given word in that document.  For instance, if our corpus is two sentences where one is "The dog slept quietly" and "The cat jumped over the dog", our tokenized sentences would look like this where the first value is the number of times 'the' occurs, the second the number of times 'dog' occurs, etc.:

    Sentence 1: [1, 1, 1, 1, 0, 0, 0]
    Sentence 2: [2, 1, 0, 0, 1, 1, 1]

The [20 Newsgroups Data Set](https://archive.ics.uci.edu/ml/datasets/Twenty+Newsgroups) is a studied data set in the machine learning community, offering 20k comments taken from 20 different news subjects.  Let's find the latent features in it by first turning our documents into vectors and then pulling out the top 10 features.  You don't need to understand all of this code, just the intuition behind it:

        from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
        from sklearn.decomposition import NMF
        from sklearn.datasets import fetch_20newsgroups
        from time import time

        n_samples, n_features, n_topics, n_top_words = 2000, 1000, 10, 20

        def print_top_words(model, feature_names, n_top_words):
            for topic_idx, topic in enumerate(model.components_):
                print("Topic #%d:" % topic_idx)
                print(" ".join([feature_names[i]
                                for i in topic.argsort()[:-n_top_words - 1:-1]]))
            print()

        def nmf_20_newsgroups():
            '''
            Load the 20 newsgroups dataset and vectorize it. We use a few heuristics
            to filter out useless terms early on: the posts are stripped of headers,
            footers and quoted replies, and common English words, words occurring in
            only one document or in at least 95% of the documents are removed.
            '''
            print("Loading dataset...")
            dataset = fetch_20newsgroups(shuffle=True, random_state=1,
                                         remove=('headers', 'footers', 'quotes'))
            data_samples = dataset.data[:n_samples]

            # Use tf-idf features for NMF.
            print("Extracting tf-idf features for NMF...")
            tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
                                               max_features=n_features,
                                               stop_words='english')
            tfidf = tfidf_vectorizer.fit_transform(data_samples)
            nmf = NMF(n_components=n_topics, random_state=1,
                      alpha=.1, l1_ratio=.5).fit(tfidf)

            print("\nTopics in NMF model:")
            tfidf_feature_names = tfidf_vectorizer.get_feature_names()
            print_top_words(nmf, tfidf_feature_names, n_top_words)

        nmf_20_newsgroups()

Take a look at what's going on in this code's output.  The terms you see printed are those that are most correlated to a given topic.  In practice, it'd be up to you to label those terms with an appropriate topic.  Can you see how this technique could be helpful in other applications like segmenting customers?

Step 3: Multiprocessing to Get Latent Features
------

Now let's take a look at multiprocessing.  Unlike threading, where we created a number of threads and our processor toggled between them when possible, multiprocessing creates separate processes that cannot share information across them.  Multiprocessing is therefore appropriate for more computationally expensive tasks.  The general idea is that we create a pool of processes.  We then map some function and an iterable across our pool.  Read through this code and then run it:

        import numpy as np
        import multiprocessing
        from time import sleep

        cpu_count = multiprocessing.cpu_count()
        print("This machine has {} cpu's".format(cpu_count))

        def some_function(i):
            sleep(i)
            print("Job finished. I just slept for {} seconds".format(i))

        iterable = np.ones(cpu_count) * 3

        pool = multiprocessing.Pool(processes=cpu_count)
        outputs = pool.map(some_function, iterable)

If you have time, you can play around with this by running `top` in another window and watching the separate processes spin up.

Now let's apply this to our news sources.  Pass your list of documents as strings through this code.  Then try multiprocessing it to see if there's a speedup.  Our dataset might be too small to see a big speedup, so you can use the function from step 2 to run NMF multiple times and see the difference.

        def return_topics(l):
            '''
            INPUT: List of lists where each list is document in a corpus
            OUTPUT: None, prints top latent topics
            '''
            n_features, n_topics, n_top_words = 1000, 10, 5
            # Use tf-idf features for NMF.
            print("Extracting tf-idf features for NMF...")
            tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
                                               max_features=n_features,
                                               stop_words='english')
            tfidf = tfidf_vectorizer.fit_transform(l)
            nmf = NMF(n_components=n_topics, random_state=1,
                      alpha=.1, l1_ratio=.5).fit(tfidf)

            print("\nTopics in NMF model:")
            tfidf_feature_names = tfidf_vectorizer.get_feature_names()
            print_top_words(nmf, tfidf_feature_names, n_top_words)

Stretch Goal: Work with your colleagues to get a separate corpus for each news source and see what different news outlets are discussing

#### On completing this assignment, you should have submitted:

- Cleaned code showing how your downloaded your stored websites and parsed out the article content in the form of a `.py` file
- Code showing you completed steps 2 and 3 with the latent topics you found
