"""
Step 1)
Manually create EMR cluster 
And dennnnn
Step 2)
scp this script to our master node
scp -i ~/.ssh/EC2_SSH_key_pair.pem /Users/adamszabunio/sandbox/lab7_1.py hadoop@ec2-54-173-152-31.compute-1.amazonaws.com:~
lab7_1.py                                 100% 1701    21.4KB/s   00:00

Step 3)
ssh into our master node
ssh -i ~/.ssh/EC2_SSH_key_pair.pem hadoop@ec2-54-159-215-49.compute-1.amazonaws.com

Step 4)
[hadoop@ip-172-31-77-230 ~]$ spark-submit lab7_1full.py > output
"""


import json
from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext("local[*]") #make SparkContext
spark = SparkSession(sc) #allows toDF

# rdd = sc.textFile("test") # localfile
rdd = sc.textFile("s3a://nobucketforyou/2017/03/31/18/*")

def mapper(line):
    dick = str(line)
    dick1 = json.loads(dick)
    text = dick1.get('text')
    lang = dick1.get('lang')
    if lang == 'en':
        lang = 0
    elif lang == 'es':
        lang = 1
    return text, lang

df = rdd.map(mapper).filter(lambda x : x[1] == 0 or x[1] == 1).toDF(['tweet', 'lang']).cache()

from pyspark.ml.classification import RandomForestClassifier
import pyspark.ml.evaluation as ev
from pyspark.ml.feature import RegexTokenizer, HashingTF, IDF
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

tweets_train, tweets_test = df.randomSplit([0.7, 0.3], seed=123)
model = pipeline.fit(tweets_train)
test_model = model.transform(tweets_test)

evaluator = ev.BinaryClassificationEvaluator(rawPredictionCol='probability', labelCol='lang')
print('AUC for Random Forest:', evaluator.evaluate(test_model, {evaluator.metricName: 'areaUnderROC'}))

model.save('s3a://nobucketforyou/models/model_7_1')
# pipeline.save('s3a://nobucketforyou/models/pipeline_7_1')

sc.stop()
