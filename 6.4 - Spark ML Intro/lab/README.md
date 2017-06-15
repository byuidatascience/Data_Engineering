Machine Learning at Scale
---------

A typical data science pipeline often includes prototyping a model in python using a library like `sklearn`.  The next step is often either refactoring the code in a lower level language or launching it into production.  This works well on smaller datasets or if you're comfortable using a subset of your data for prototyping.  What happens, however, if your data is too large to fit on a single machine?  What happens when you need to retrain your model periodically?  Recommender systems are a great example of this business use (check out the [Netflix Challenge](http://www.netflixprize.com/), a great case study on recommenders with large datasets).

Today, we'll be making a simple end-to-end model to classify the language of a tweet as either Spanish or English.  In the next lab, we'll be bundling this up into a `spark-submit` job that we can run as a batch process.

### Step 1: Understanding the Spark ML Pipeline

Recall that there are three main abstract classes in [Spark's ML library](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html):

1. `Transformers`: transforms your data by (normally) appending a new column to your DataFrame.
2. `Estimators`: these are the statistical models that we estimate.  The ML library has a suite of classification, regression, and clustering algorithms.
3. `Pipelines`: offers an end-to-end transformation-estimation process with distinct stages.  A pipeline will ingest raw data in the form of a DataFrame and perform the necessary transformations in order to estimate a statistical model.  A pipeline often consists of multiple transformers that feed into an estimator

We'll be addressing each of these three classes in our script.

### Step 2: Preparing our Data

The following steps will help us prepare our data for downstream analysis.

1. Spin up an EMR cluster with Zeppelin and Spark.  You might want to refer to [lab 4.3](4.3%20-%20Spark%20Overview/lab) for details.
2. Open a Zeppelin notebook and import an hour's worth of raw tweets from s3 as an RDD
3. Transform your data so that you have two values: `tweet` (your tweet text) and `lang`.  `lang` should be a 0 if English or 1 if Spanish.  You can disregard all other tweets
4. Create a DataFrame out of this using the `toDF` method and cache it
5. Create a train/test split with 70% of your data in your training set and 30% of your data in your test set.  You code should look something like this: `tweets_train, tweets_test = df.randomSplit([0.7, 0.3], seed=123)`.  Take a moment to ask what the `seed` is here and why it's important.

### Step 3: Building our Pipelines

A pipeline allows you to chain together the steps of your model, making it easy to apply the same transformations and actions to different data.  Take a look at the code below that implements [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) and uses random forest to try to predict the language used.

Similar to our [muliprocessing lab](3.3%20-%20Multiprocessing/lab/README.md), we'll first be turning our tweets into tokens and removing punctuation.  We'll then use the [`HashingTF` function](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html?highlight=hashingtf#pyspark.ml.feature.HashingTF) to calculate the frequency of words in our corpus (see [this article](https://en.wikipedia.org/wiki/Feature_hashing) on the difference between our tokenizing in 3.3 and today's lab).  The inverse document frequency will offset the term frequency by how frequently a given word appears in a tweet.  Finally, we'll be passing this to random forest to build a model off of these two calculations.

        from pyspark.ml.feature import RegexTokenizer, HashingTF, IDF
        from pyspark.ml.classification import RandomForestClassifier
        from pyspark.ml import Pipeline


        tokenizer = RegexTokenizer(inputCol="tweet", outputCol="words", pattern='\s+|[,.\"]')
        hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=200)
        idf = IDF(inputCol="rawFeatures", outputCol="features")
        forestizer = RandomForestClassifier(labelCol="lang", featuresCol="features", numTrees=10)

        pipeline = Pipeline(stages=[\
                        tokenizer,
                        hashingTF,
                        idf,
                        forestizer])

After getting a sense for how this pipeline works, fit your training set to it using `model = pipeline.fit(tweets_train)`.  This model could take quite a while to train depending the size of our data (it took about an hour to run on 9M tweets).

### Step 4: Evaluating and Saving Our Model

Let's first evaluate our results and then save our pipeline and model so that we don't lose it when take our cluster down.  To evaluate our result, we first need to use our model to predict on our test set and then we'll calculate the [Area Under the ROC Curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic), a common evaluation metric for classification problems that uses true and false positive rates.

        import pyspark.ml.evaluation as ev

        test_model = model.transform(tweets_test)
        evaluator = ev.BinaryClassificationEvaluator(rawPredictionCol='probability', labelCol='lang')
        print('AUC for Random Forest:', evaluator.evaluate(test_model, {evaluator.metricName: 'areaUnderROC'}))

Make a note of what your score was.  Around .9 is to be expected depending on how much data you fed to you model.

Now let's save our pipeline and model.  You can use `.save('s3a://bucket/path')` to accomplish this.  Check s3 to take a peek at how it works.


### Stretch Goal: Connecting to postgres with Spark

We've seen how to insert data into `postgres` using `psycopg2`.  An alternative to this pythonic way of connecting is the more sparkic (a term I just made up) way of using [theJDBC driver](https://github.com/apache/zeppelin/blob/master/docs/interpreter/jdbc.md).  Try connecting to postgres using JDBC instead.   

----

#### On completing this assignment, you should have submitted:

- A .json file with your model.  Submit only the bare minimum code to get your model running as we'll be using this as a spark submit job in the next lab
