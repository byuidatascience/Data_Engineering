Welcome to Data Engineering!
===

#### By the end of this article you should have:

- Watched:
    - Creating An AWS Account - Part 2
- Read (in addition to this article):
    - Create Virtual Environments for Python with Conda
- Completed:
    - Obtained a consumer key, consumer secret, access token, and access token secret from Twitter

Set up AWS
------

By now you have already completed the [pre-course assignment](../0.0 - Prework/README.md) of setting up your AWS account and activating your free credit. In doing so, you should have watched [What Is The Cloud?](http://infiniteskills.bc.cdn.bitgravity.com/iskills-media/awscloud-demo/0101.mp4) and [Cloud Computing Basics](http://infiniteskills.bc.cdn.bitgravity.com/iskills-media/awsintro-demo/0101.mp4) (if you haven't, go do that now). You also should have watched [Creating An AWS Account - Part 1](http://infiniteskills.bc.cdn.bitgravity.com/iskills-media/awsintro-demo/0104.mp4). Now watch [Part 2](http://infiniteskills.bc.cdn.bitgravity.com/iskills-media/awsintro-demo/0105.mp4). This will prepare you for the [lab](lab/README.md) on the first day of class.

Create a Twitter App
------

If you do not already have a Twitter account, create one now at [twitter.com/signup](https://twitter.com/signup)

Go to [apps.twitter.com/app/new](https://apps.twitter.com/app/new) and create an "application". Some notes:  

- The name of your app doesn't matter, but it must be unique
- The website URL doesn't matter either, though it must be valid

We will not be using this until day 2, but since it sometimes takes time for the app to be approved, you will want to do this ahead of time.

Conda Environments
---

For this course, we will need to create a new conda environment. Conda environments are an extension of virtual environments (not to be confused with virtual *machines* which we will discuss separately in this course). Virtual environments allow you to specify which packages and which versions you will use for your application (for example, Python 2 instead of Python 3, and boto3 but not scikit-learn). This is useful both for avoiding version conflicts and for help in deploying code as you more easily make sure that your environment matches that on the machine to which you will be deploying.

Setting this up and installing the necessary packages will be the first part of our first [lab](lab/README.md) assignment. This was already covered in a previous course, but if you feel like you need a refresher, read how to [create virtual environments for python with conda](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/).

---

#### On completing this article, you should have:

- Watched one video about AWS
- Created an account for a Twitter "app"
- Optional: Read one blog article about conda environments

Finally, here are some resources about data engineering in general to whet your appetite for what's to come.  
(_These are also optional._)  

- Watch: [Bridging the Gap Between Data Science and Data Engineering](https://www.youtube.com/watch?v=EtYv7zPyS2A)
- Read: [What’s the Difference Between Data Engineering and Data Science?](http://www.galvanize.com/blog/difference-between-data-engineering-and-data-science/)
- Read: [Data Scientist, Data Engineers, & Infrastructure Engineers](http://multithreaded.stitchfix.com/blog/2016/03/16/engineers-shouldnt-write-etl/)
- Watch: [Data Engineering @ Slack](https://drive.google.com/file/d/0BxGB59WxQI5oTXpQd09jbVpvalE/view)  
