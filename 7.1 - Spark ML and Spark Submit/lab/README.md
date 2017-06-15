Batch Processing ML Jobs
---------

One distinct advantage of Spark over Hadoop is that we can interact with our data in real time.  In the past, we've used both Zeppelin and Jupyter notebooks to do this.  This works well when we're prototyping, but what about when we want to update an ML model daily?  The preferred way to do this is as a `spark-submit` job.  The goal of this lab is to retrain our ML model from the last lab on the most recent tweets.

### Step 1: Spinning up EMR Programatically

Instead of using the AWS Console, we can spin up a cluster at the command line.  To do this, you'll want to use a command like this:

        aws emr create-cluster --release-label emr-5.5.0 --applications Name=Spark --instance-type m3.xlarge --instance-count 5 --service-role EMR_DefaultRole --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole,KeyName=<key name> --configurations https://s3.amazonaws.com/conor-sandbox/myConfig.json

Be sure to insert your key name without the `.pem` suffix (i.e. `snuffaluffagus_key` not `snuffaluffagus_key.pem`).  The configurations file, which you have access to, looks like this.  You can edit it and save it to your own s3 bucket if you'd like to change it.

        [
            {
              "Classification": "spark-defaults",
              "Properties": {
                "spark.executor.memory": "15G"
              }
            }
          ]

You should receive a `ClusterId` after running this code.  Once the cluster has started, you can grab the public DNS with `aws emr list-instances --cluster-id j-XXXXXXXXXXX`.  It will take a minute to start up.  Don't forget to tear this cluster down at the end of the day as we're starting to scale out into some serious firepower.

### Step 2: Connecting to our Cluster

SSH into the master node of this cluster.  When you run the `list-instances` command, you should be able to tell the master node by the fact that it has a different `InstanceGroupId`.  The user name that you're signing in to is `hadoop`.

### Step 3: Submitting a `spark-submit` job

One major difference between using REPL's like Zeppelin is that they gave us a `SparkContext` already defined.  This is our main entry point into Spark.  When submitting a `spark-submit` job, we must define this for ourselves.  The simplest form of this is `sc = SparkContext("local[*]")`, but look at [the documents](http://spark.apache.org/docs/latest/api/python/pyspark.html?highlight=sparkcontext#pyspark.SparkContext) for more nuance as needed.  Run through [the examples here](http://blog.appliedinformaticsinc.com/how-to-write-spark-applications-in-python/) to get a simple job running.  You can also get jobs running locally as well.

### Step 4: Training an ML Model

Refactor your code from last week to run as a `spark-submit` job.  You'll need to define your `SparkContext` and run `sc.stop()` at the end.  Since spark ML uses DataFrames, we'll need to import a `SparkSession` too.  Import `SparkSession` from `pyspark.sql` and initialize it after defining your `SparkContext` with `spark = SparkSession(sc)`.  Otherwise, this code should very similar to what you did in the last lab.  Once you've got it working, you may wish to look at the Deploying guide to [Submitting Applications](http://spark.apache.org/docs/latest/submitting-applications.html) but probably not before.  

### Stretch Goal: Running `spark-submit` Jobs Remotely

Read back through [Submitting User Applications with spark-submit](https://aws.amazon.com/blogs/big-data/submitting-user-applications-with-spark-submit/) and submit a `spark-submit` job from your local machine.

#### On completing this assignment, you should have submitted:

- Your deliverable for this lab is the python file you submit along with instructions on how to run it. Those instructions can either be in a comment block in your python file or in a separate file.
