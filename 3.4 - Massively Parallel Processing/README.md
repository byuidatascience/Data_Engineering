Scaling Out
-----

#### By the end of this article you should have:

- Watched:
    - the 2nd hour of Advanced Machine Learning with scikit-learn
- Read:
    - Using `ipyparallel`

---

The Python library I like to use for simple parallel processing (which we will be using for our lab) is [`ipyparallel`](http://ipyparallel.readthedocs.io/en/latest/intro.html). I like it because it is relatively easy to use and also because it can scale to a multi-node architecture without changing anything. (That is, once it knows about other nodes running ipython engines, it can treat them all as if they were on one giant computer.) This tool was developed about a decade ago (long before Hadoop and Spark) and is still the most efficient way to parallelize Python across a cluster. It is not nearly as robust as Hadoop or even Spark, but it works well for a lot of problems (such as grid search and cross-validation).

Watch Olivier Grisel's tutorial on [Advanced Machine Learning with scikit-learn](https://www.youtube.com/watch?v=iFkRt3BCctg&feature=youtu.be&t=1h3m28s) from 1:03:28 to 1:54:52. (You may want to watch the first hour as well if you feel like you need a review of machine learning concepts for 6003.) In the tutorial, Olivier is using an older version of IPython which had the parallel module included (as `IPython.parallel`). Since then, that module has been made into its own library called `ipyparallel`. A few other updates have been made, so watch out for that, but the fundamentals are the same. (Just replacing `IPython.parallel` with `ipyparallel` works much of the time.)

Once you've completed that, read through this primer on [Using `ipyparallel`](http://people.duke.edu/~ccc14/sta-663-2016/19C_IPyParallel.html) (actually, the whole course on [Computational Statistics in Python](http://people.duke.edu/~ccc14/sta-663-2016/index.html) is probably worth bookmarking).

**Optional:** This weekend would be a good time to go through lesson 2 in the Cloud Computing Concepts course we started last week with the following two lectures:

1. [A cloud IS a distributed system](https://www.coursera.org/learn/cloud-computing/lecture/DI6AV/2-1-a-cloud-is-a-distributed-system)
2. [What is a distributed system?](https://www.coursera.org/learn/cloud-computing/lecture/nvMXE/2-2-what-is-a-distributed-system)

Though not required for this lesson, they will help prepare you for next week.

---

#### On completing this article, you should have:

- Watched the second half of one video
- Read one lesson from Computational Statistics in Python
