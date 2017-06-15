I ♥ Logs
----

#### By the end of this article you should have:

- Watched:
    - I ♥ Logs: Apache Kafka and Real-Time Data Integration
    - Introducing Amazon Kinesis Firehose

----

This week, we have started migrating our code to the cloud. We've been relying on a third-party API to answer our queries, but let's say we don't trust it (could the trending topics be doctored? How would we know?) or we want to answer questions that cannot be answered by the API (how many unique users post tweets in a given day?). In order to answer these questions, we will need to access the raw data. Accessing the raw data means increasing the volume and the velocity of the data, and also going from structured to semi-structured data (increasing the variety). We won't be able to store all this data on a single machine. Instead, we will want to store our data on something like a distributed file system (DFS). For the time being, we will use S3 (which is "something like a distributed file system").

In order to solve these problems (multiple dedicated machines and streaming data into a DFS or S3) we will need something called a message broker to move the data around. For the purposes of this course, we will be focussing on two such systems: Apache Kafka and Amazon Kinesis. Beginning with Apache Kafka, watch this video by Jay Kreps, the author of Apache Kafka, called [I ♥ Logs: Apache Kafka and Real-Time Data Integration](https://www.youtube.com/watch?v=aJuo_bLSW6s). By the end of this video, you should understand essentially what [Kafka](https://kafka.apache.org/) is and what makes it valuable.

Now that you know what a message broker is, watch [Introducing Amazon Kinesis Firehose](https://www.youtube.com/watch?v=YQR_5W4XC94). [Amazon Kinesis ](https://aws.amazon.com/kinesis/) is Amazon's version of Apache Kafka (sort of). With Kafka we would need to program both a producer and a consumer. With [Kinesis Streams](https://aws.amazon.com/kinesis/streams/) we would do the same, but with [Kinesis Firehose](https://aws.amazon.com/kinesis/firehose/), the consumer is already defined and you just need to pick a destination (S3 or Redshift).

For a primer on Kinesis, you may wish to complete Qwiklab's [Introduction to Amazon Kinesis Firehose](https://run.qwiklab.com/focuses/2988). It's optional but may be helpful, particularly if you get stuck during the lab. One difference worth noting, however, is that Qwiklab's lab uses the [Kinesis Agent](http://docs.aws.amazon.com/firehose/latest/dev/writing-with-agents.html) while I recommend you use [boto3](http://boto3.readthedocs.io/en/latest/reference/services/firehose.html) for the class lab.

#### On completing this article, you should:

- Have watched two videos.
- Be able to identify the relationship between Kafka and Kinesis and explain what they are and why they exist.
