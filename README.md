# DSCI 6007: Distributed and Scalable Data Engineering

Welcome to Intro to Data Engineering!

_See [syllabus.md](syllabus.md) for the current syllabus._

## Schedule Overview
Organized by weeks and days:  
(_subject to change;  
see detailed schedule [below](#detailed-schedule)_)

1. [Welcome to Data Engineering](#week-1-welcome-to-data-engineering)  
    1. [Data Engineering Overview](1.1%20-%20Course%20Overview)
    2. [How the Internet Works](1.2%20-%20The%20Internet)
    1. [Virtualization](1.3%20-%20Virtualization)
    2. [Linux](1.4%20-%20Linux)
2. [The Cloud](#week-2-the-cloud)
    1. [The Cloud](2.1%20-%20The%20Cloud)
    2. [Deployment](2.2%20-%20Deployment)
    3. [Big Data Architecture](2.3%20-%20Big%20Data%20Architecture)
    4. [Review Day](2.4%20-%20Projects) - _Project Data Due_
3. [Parallel Processing](#week-3-parallel-processing)
    1. [Functional Programming](3.1%20-%20Functional%20Programming)
    2. [Threading](3.2%20-%20Threading)
    3. [Multiprocessing](3.3%20-%20Multiprocessing)
    4. [Massively Parallel Processing](3.4%20-%20Massively%20Parallel%20Processing)
4. [MapReduce (Divide-and-conquer for Distributed Systems)](#week-4-mapreduce-divide-and-conquer-for-distributed-systems)
    1. [The MapReduce Algorithm & Hadoop](4.1%20-%20MapReduce%20Intro)
    2. [MapReduce Design Patterns](4.2%20-%20MapReduce%20Design%20Patterns)
    3. [Spark Overview](4.3%20-%20Spark%20Overview)
    4. [Review Day](4.4%20-%20Proposals) - _Project Proposals Due_
5. [SQL (The Lingua Franca of Data)](#week-5-sql-the-lingua-franca-of-data)
    1. [SQL Fundamentals](5.1%20-%20SQL%20Fundamentals)
    2. [Extract Transform Load](5.2%20-%20ETL)
    3. [Relational Data Modeling](5.3%20-%20Relational%20Data%20Modeling)
    4. [Advanced Querying](5.4%20-%20Advanced%20Querying)
6. [Spark (What to add to your LinkedIn profile)](#week-6-intro-to-spark)
    1. [Spark DataFrames](6.1%20-%20Spark%20DataFrames)
    2. [Spark SQL](6.2%20-%20Spark%20SQL)
    3. [Review Day](6.3%20-%20Review)
    4. [Intro to Spark ML](6.4%20-%20Spark%20ML%20Intro)
7. [Streaming (Everyone **has to have** real-time)](#week-7-streaming-everyone-has-to-have-real-time)  
    1. [More Spark ML](7.1%20-%20Spark%20ML)
    2. [Spark Streaming](7.2%20-%20Spark%20Streaming)
    3. [Probabilistic Data Structures](7.3%20-%20Probabilistic%20Data%20Structures)
    4. [Review Day](7.4%20-%20Review)
8. [Final Project Presentations](8.1%20-%20Final%20Project)

## Detailed Schedule

### Week 1: Welcome to Data Engineering  

| Day      | Readings | Notes      | Assignment |
|:--------:|:-------- |:---------- |:---------- |
| Monday   | [Data Engineering Overview](1.1%20-%20Course%20Overview/README.md) | 1. [Intro to Data Engineering](1.1%20-%20Course%20Overview/lecture_intro_to_data_engineering.ipynb) <BR /> 2. [Intro to the Cloud](1.1%20-%20Course%20Overview/lecture_intro_to_the_cloud.ipynb) | [Conencting to the Cloud with Python](1.1%20-%20Course%20Overview/lab/README.md) |
| Tuesday  | [How the Internet Works](1.2%20-%20The%20Internet/README.md) | [How the Web Works](http://slides.com/wesleyreid/how-the-web-works) | [Generating Reports](1.2%20-%20The%20Internet/lab/README.md) |
| Thursday | [Virtualization](1.3%20-%20Virtualization/README.md) | [Virtualization & Docker](1.3%20-%20Virtualization/lecture_virtualization.ipynb) | [Your Very Own Web Server](1.3%20-%20Virtualization/lab/README.md) |
| Friday   | [*NIX](1.4%20-%20Linux/README.md) | [Linux](1.4%20-%20Linux/lecture_linux.ipynb) | [Linux Intro](1.4%20-%20Linux/lab/README.md) |

### Week 2: The Cloud

| Day      | Readings | Notes      | Assignment |
|:--------:|:-------- |:---------- |:---------- |
| Monday   | [Introduction to Clouds](2.1%20-%20The%20Cloud/README.md) | [The Cloud & AWS](2.1%20-%20The%20Cloud/lecture_the_cloud2_EC2.ipynb)  | [Move your Linux machine to the Cloud](2.1%20-%20The%20Cloud/lab/README.md) |
| Tuesday  | [Provisioning](2.2%20-%20Deployment/README.md) | [EC2 & cron](2.2%20-%20Deployment/lecture_cron_ec2.ipynb) | [Automate More](2.2%20-%20Deployment/lab/README.md) |
| Thursday | [I ♥ Logs](2.3%20-%20Big%20Data%20Architecture/README.md) | [Apache Kafka](2.3%20-%20Big%20Data%20Architecture/lecture_kafka.ipynb) | [Drinking from the Firehose](2.3%20-%20Big%20Data%20Architecture/lab/README.md) |
| Friday | [Projects](2.4%20-%20Projects/README.md) | [Project Proposal](2.4%20-%20Projects/project_proposal.ipynb) | [Proposal](2.4%20-%20Projects/lab/README.md) |

### Week 3: Parallel Processing

| Day      | Readings | Notes      | Assignment |
|:--------:|:-------- |:---------- |:---------- |
| Monday   | [Functional Programming](3.1%20-%20Functional%20Programming/README.md) | | [Fun with Toolz](3.1%20-%20Functional%20Programming/lab/README.md)
| Tuesday  | [Threading and Webscraping](3.2%20-%20Threading/README.md) | | [Threading and Webscraping](3.2%20-%20Threading/lab/README.md) |
| Thursday | [Intro to Multiprocessing](3.3%20-%20Multiprocessing/README.md) | [Multiprocessing Demonstration](3.3%20-%20Multiprocessing/Multiprocessing%20Demonstration.ipynb) | [Multiprocessing](3.3%20-%20Multiprocessing/lab/README.md) |
| Friday   | [Scaling Out](3.4%20-%20Massively%20Parallel%20Processing/README.md) | [Distributed Computing](3.4%20-%20Massively%20Parallel%20Processing/lecture_distrbuted_systems.ipynb) | [Embarrassingly Parallel](3.4%20-%20Massively%20Parallel%20Processing/lab/README.md) |

### Week 4: MapReduce (Divide-and-conquer for Distributed Systems)

| Day      | Readings | Notes      | Assignment |
|:--------:|:-------- |:---------- |:---------- |
| Monday   | [HDFS and MapReduce](4.1%20-%20MapReduce%20Intro/README.md) | [MapReduce](4.1%20-%20MapReduce%20Intro/lecture_map_reduce.ipynb) | [Scaling Out](4.1%20-%20MapReduce%20Intro/lab/README.md) |
| Tuesday  | [MapReduce Design Patterns](4.2%20-%20MapReduce%20Design%20Patterns/README.md) | [Hadoop Ecosystem](4.2%20-%20MapReduce%20Design%20Patterns/lecture_hadoop_ecosystem.ipynb) | [Meet MrJob](4.2%20-%20MapReduce%20Design%20Patterns/lab/README.md) |
| Thursday | [Introduction to Spark](4.3%20-%20Spark%20Overview/README.md) | [Apache Spark](4.3%20-%20Spark%20Overview/lecture_spark_intro_rdd.ipynb) | [Spark on EMR](4.3%20-%20Spark%20Overview/lab/README.md) |
| Friday   | [Designing Big Data Systems](4.4%20-%20Proposals/README.md) | [Review](4.4%20-%20Proposals/review_questions_and_answers.ipynb) | [Final Project Proposal](4.4%20-%20Proposals/lab/README.md) |

### Week 5: SQL (The Lingua Franca of Data)

| Day      | Readings | Notes      | Assignment |
|:--------:|:-------- |:---------- |:---------- |
| Monday   | [SQL Basics](5.1%20-%20SQL%20Fundamentals/README.md) | [Databases and SQL](5.1%20-%20SQL%20Fundamentals/lecture_sql_fundmentals.ipynb) | [Squashing Birds](5.1%20-%20SQL%20Fundamentals/lab/README.md) |
| Tuesday | [Relational Design](5.3%20-%20Relational%20Data%20Modeling/README.md) | [Relational Database Modeling](5.3%20-%20Relational%20Data%20Modeling/lecture_relational_model.ipynb) | [Data Modeling Practice](5.3%20-%20Relational%20Data%20Modeling/lab) |
| Thursday  | [Drivers and Workers](5.2%20-%20ETL/README.md) | [SQL: Advanced Querying](5.2%20-%20ETL/lecture_sql_advanced_querying.ipynb) | [Feeding the Elephant](5.2%20-%20ETL/lab/README.md) |
| Friday   | [Tuning SQL](5.4%20-%20Advanced%20Querying/README.md) | [Data Systems Architecture](5.4%20-%20Advanced%20Querying/lecture_sql_optimization.ipynb) | [Advanced Querying](5.4%20-%20Advanced%20Querying/lab/README.md) |

### Week 6: Spark (What to add to your LinkedIn profile)

| Day      | Readings | Notes      | Assignment |
|:--------:|:-------- |:---------- |:---------- |
| Monday   | [Spark DataFrames](6.1%20-%20Spark%20DataFrames/README.md) | [Spark](6.1%20-%20Spark%20DataFrames/lecture_spak_dataframes.ipynb) | [DataFrames](6.1%20-%20Spark%20DataFrames/lab/README.md) |
| Tuesday  | [Programming with RDDs](6.2%20-%20Spark%20SQL/README.md) | [Spark SQL](6.2%20-%20Spark%20SQL/lecture_spark_sql.ipynb) | [Spark SQL](6.2%20-%20Spark%20SQL/lab/README.md) |
