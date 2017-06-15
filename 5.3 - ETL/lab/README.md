Feeding the Elephant
-----

In the past two labs we used a python script to put a small amount of data into our Postgres database using `psycopg2`.  This works well on a small amount of data, but since this was a serial process it won't scale well.  We could use threading to improve our script from yesterday but we would still be limited to a single machine.  Today we will use Spark to load our database instead so we can take full advantage of distributed processing.

### Step 0: Start a Spark Cluster with psycopg2

We are going to spin up another Spark cluster using EMR, but this time we need to [Go to advanced options](https://console.aws.amazon.com/elasticmapreduce/home?region=us-east-1#create-cluster:).
1. Select Spark and Zeppelin. (You can uncheck Pig and Hue, we don't need them.) Click "Next".
2. You may increase the number of Core nodes. Click "Next" again.
3. Open "Bootstrap Actions" at the bottom (be careful, it's easy to miss), select "Custom action", and click "Configure and add". Enter "s3://dsci/6007/bin/install-psycopg2.sh" as the Script location. (_N.B._ you will not be able to navigate to this because you don't own this bucket, but you should still be able to use this script.)
4. Select your EC2 key pair. (You probably won't need it but it's always good to have.) And "Create Cluster"

This will create a new Spark cluster with the `psycopg2` module already installed on each node.

If this doesn't work for you, you can always add a step later using the `command-runner.jar`.

Alternatively, you may use the Postgres JDBC driver. See [Using pyspark to connect to PostgreSQL](http://stackoverflow.com/questions/34948296/using-pyspark-to-connect-to-postgresql) for details. (If you do that, the following steps must be changed accordingly since you will no longer be using `psycopg2`.)

### Step 1: Convert your Python script into PySpark

Take the code you developed from yesterday's lab and convert it into a function that can be passed to RDD partitions. There are a few important things to note here:

- You must:  
    1. `import psycopg2`  
    2. `connect` to your database.  This should look something like this:

        conn = psycopg2.connect(**{'dbname': 'postgres',
                             'host': 'postgres.XXXXX.us-east-1.rds.amazonaws.com',
                             'password': 'XXXXX',
                             'user': 'XXXXX'})

    3. create a `cursor` within the function. Remember, there is no shared state outside of a worker. Each one is running it's own instance of Python.
- Use the `foreachPartition` method.
    - If you try to `collect` all the data and then insert it, you will likely run out of memory. You want to do this in a distributed fashion.
    - If you try to use `foreach` (instead of `foreachPartition`) you will be creating a database connection for each row and quickly exhaust your connection pool. Postgres will happily accept as many connections as you have partitions, but it will not accept as many connections as you have rows.

This step is a little tricky so be careful with it and don't be afraid to ask for help.

Don't forget to test your code on a subset of your data first! You don't want to have to wait for it to chunk through over a 100 GiB of data only to find it didn't work.

### Step 2: Package this into a batch process (optional)

Being able to interact with data using the Spark REPL (or, in our case, Zeppelin notebook) is extremely valuable. But there are times when you want to just run a job as a batch process.

In order to do this, we will use the `spark-submit` utility. This should be run on the master node of your Spark cluster. Take a look at [How To Write Spark Applications in Python](http://blog.appliedinformaticsinc.com/how-to-write-spark-applications-in-python/). Note that the documentation for `spark-submit` allows for a lot of options you don't need, so try not to get distracted by that.

Note: You may need to `unset PYSPARK_DRIVER_PYTHON` in order to prevent `spark-submit` from trying to launch Jupyter. You may also need to specify `sc = SparkContext()` in this case.

Once you've got it working, you may wish to look at the Deploying guide to [Submitting Applications](http://spark.apache.org/docs/latest/submitting-applications.html) but probably not before.

### Step 3: Use Airflow (or cron) to control EMR (optional)

Finally, to fully automate this process, we will want to set this up in such a way so that our tiny EC2 instance can--once a day--spin up an EMR cluster, run this script on the latest data, and shut that cluster down.

Your deliverable for this lab is the python file you submit along with instructions on how to run it. Those instructions can either be in a comment block in your python file or in a separate README.

----

#### On completing this assignment, you should have submitted:

- A Zeppelin notebook (`.json`) or executable PySpark script (`.py`) that populates the tables in your postgres database
