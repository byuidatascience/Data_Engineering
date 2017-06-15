Threading and Webscraping
-------------------------

#### By the end of this assignment you should have:

- Used the `requests` library to get data from news websites
- Stored a large number of articles in a publicly readable s3 bucket
- Used the `threading` library to speed up our scraping

Introduction
------

In this assignment we will scrape news websites for their data.  In the past, we have used the twitter API to collect data.  An alternative to this would be to download websites and store them in s3 so that we can extract data from them downstream.  Since webscraping is an **I/O bound problem** in that the biggest limitation to our work is the transfer of information across a network, we can speed up this process using threading.

Certain websites, especially high traffic websites like the ones we'll be scraping, take steps to avoid webscrapers.  This creates a fun cat-and-mouse game of trying to grab data.  Note that tools like **Tor** and **Selenium** exist for really hard sites to crack.  While not necessary for this lab, it's good to know they exist.

Step 1 : Divide news websites
-------

Here are the twitter handles for a few major news websites with their respective biases.  You can use [Alexa](http://www.alexa.com/topsites/category/News) to source additional sites if you feel so inclined:

Minimal partisan bias:
- NYTimes
- BBCWorld

High liberal bias:
- OccupyDemocrats ‏
- AddInfoOrg

High conservative bias:
- FoxNews
- BrietbartNews

Divide these three groups of sites among the pairs so that no fewer than 2 pairs are working on each set.  If you want to add sites to your list, feel free to do so but you must at least scrape both sites from one of the categories above.

In Google chrome, navigate to an article on these sites and then go to `View -> Developer -> Developer Tools`.  Play around with this function by scrolling over the different components of the website so you can how it works.  You browser uses the HTML tags and CSS (Cascading Style Sheet) to render a website.  This structure will help us to extract the data we want.

Step 2: Build a Webscraper
-------

Recall from our reading for 1.2 that HTTP is a protocol with a limited number of methods.  The most common for us will be the `GET` method:

| Method | Description                                                 |
|--------|-------------------------------------------------------------|
| `GET`  | Used to retrieve a resource, like an HTML file, from a server |
| `POST` | Used send information, like user input, to a server        |

The `requests` library will allow us to make GET requests of a website.  Here's how it works:

        import requests
        url = 'http://www.nytimes.com'
        r = requests.get(url)
        data = r.text

That was easy!  This is a great, legal way to access proprietary data.

Now, write a script that uses your code from the last lab in order to create four functions:

1. Pull as much of the twitter timeline as you can from your news sources using `t.statuses.user_timeline(screen_name=<user>, count=200)` (if you're using the [twitter](https://pypi.python.org/pypi/twitter) package)
2. Using your code from the last lab, pull all url's from those tweets
3. Make GET requests to get those articles
4. Place those articles in a publicly readable s3 bucket using boto (note that you can use the url as the name of the file but remove the `/` so s3 doesn't interpret it as a folder) **Remember that you must at least scrape your sites though you can easily add other sites once your code is working:**

Run this code on **one of your two websites** and record the time it takes by wrapping your code in:

        import time
        start = time.time()

        <your code here>

        print('This code took {} seconds'.format(time.time()-start))

Step 3: Use Threading to Speed up the Process
--------

Running different threads is similar to running different programs concurrently.  In essence, we'll define a queue of tasks (our URL's) and each thread will look to download its contents and push the results to s3.  Upon completion of a task, the thread will then look for the next item in the queue.  Using the functions you wrote above, thread the process of scraping websites and pushing the results to s3.  Here's some code to get you started:

        import queue
        from threading import Thread

        start = time.time()

        # specify sitemap to get all site links
        url_list = ['http://www.nytimes.com'] ## USE YOUR URLS HERE

        # create the queue instance and add urls to the queue
        q = queue.LifoQueue()
        [q.put(url) for url in url_list]

        # define how the URL transformations
        def grab_data_from_queue():
            while not q.empty(): # check that the queue isn't empty
                url = q.get() # get the item from the queue
                r  = requests.get(url) # request the url

                ## ADD YOUR CODE HERE

                q.task_done() # specify that you are done with the item

        # create and start threads
        for i in range(12): # aka the number of threads
            t1 = Thread(target = grab_data_from_queue) # target is the above function
            t1.start() # start the thread

        q.join()

        print('This code took {} seconds'.format(time.time()-start))

If you get stuck, here are some tips:

- [This tutorial](http://www.craigaddyman.com/python-queues-and-multi-threading/) offers a simplified version of this exercise
- Note that these sites might have ways to prevent you from webscraping.  One common method is rate limiting.  Try using `time.sleep()` to limits your calls per second
- Some sites block IPs from known bad actors.  LinkedIn, for instance, actually does this for any AWS IP address.  Tools like Tor and [its Python client](https://stem.torproject.org/tutorials.html) allow you to mask the origin of your request by daisy chaining it across a network of nodes.

Stretch Goal: push this code to an EC2 instance that periodically pulls all new urls tweeted by a list of usernames and stores the results in s3


#### On completing this assignment, you should have submitted:

- A `.py` file with functions to pull twitter data, pull urls from tweets, download articles using GET requests, and placing those articles in s3
- Documentation of the time difference between using threading and not using threading
