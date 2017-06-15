Drivers and Workers
-------

Today's lesson is short but dense. I want you to watch the middle part of [Everyday I'm Shuffling](https://www.youtube.com/watch?v=Wg2boMqLjCg&feature=youtu.be&t=15m20s) from 15:20 to 25:48. It's only ten minutes long but it's full of valuable goodness. (Later you will want to watch the first 15 minutes.) 

The first main takeaway, from Vida's part of the talk, is identifying which part of a Spark program are executed where. This is really essential to writing Spark programs that work. 

The second main takeaway, from Holden's part, is using [`foreachPartition`](http://spark.apache.org/docs/2.1.0/api/python/pyspark.html#pyspark.RDD.foreachPartition) to write data from Spark to a database. This is the pattern we will be using in today's lab, so make sure that you understand this part (specifically 21:45 to 24:32 or "the DIY approach").
