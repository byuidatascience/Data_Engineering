# KillrWeather

KillrWeather is a reference application (which we are constantly improving) showing how to easily leverage and integrate [Apache Spark](http://spark.apache.org),
[Apache Cassandra](http://cassandra.apache.org), and [Apache Kafka](http://kafka.apache.org) for fast, streaming computations in asynchronous event-driven environments. This application focuses on the use case of  **[time series data](https://github.com/killrweather/killrweather/wiki/4.-Time-Series-Data-Model)**.  

## Sample Use Case
I need fast access to historical data on the fly for  predictive modeling  with real time data from the stream.

## Time Series Data
The use of time series data for business analysis is not new. What is new is the ability to collect and analyze massive volumes of data in sequence at extremely high velocity to get the clearest picture to predict and forecast future market changes, user behavior, environmental conditions, resource consumption, health trends and much, much more.

Apache Cassandra is a NoSQL database platform particularly suited for these types of Big Data challenges. Cassandra’s data model is an excellent fit for handling data in sequence regardless of data type or size. When writing data to Cassandra, data is sorted and written sequentially to disk. When retrieving data by row key and then by range, you get a fast and efficient access pattern due to minimal disk seeks – time series data is an excellent fit for this type of pattern. Apache Cassandra allows businesses to identify meaningful characteristics in their time series data as fast as possible to make clear decisions about expected future outcomes.

There are many flavors of time series data. Some can be windowed in the stream, others can not be windowed in the stream because queries are not by time slice but by specific year,month,day,hour. Spark Streaming lets you do both.

## Start Here

### Clone the repo

    git clone https://github.com/killrweather/killrweather.git
    cd killrweather


### Build the code
If this is your first time running SBT, you will be downloading the internet.

    cd killrweather
    sbt compile

### Setup for Linux & Mac

1. [Download Apache Cassandra 2.1](http://www.apache.org/dyn/closer.lua/cassandra/2.1.14/apache-cassandra-2.1.14-bin.tar.gz) and open the compressed file.

2. Start Cassandra - you may need to prepend with sudo, or chown /var/lib/cassandra. On the command line:

    ./apache-cassandra-2.1.14/bin/cassandra -f

3. Run the setup cql scripts to create the schema and populate the weather stations table.
On the command line start a cqlsh shell:

    cd /path/to/killrweather/data  
    path/to/apache-cassandra-2.1.14/bin/cqlsh

### Setup for Windows

1. [Download the latest Cassandra](http://www.planetcassandra.org/cassandra) and double click the installer.

2. Chose to run the Cassandra automatically during start-up

3. Run the setup cql scripts to create the schema and populate the weather stations table.
On the command line start a cqlsh shell:

    cd c:/path/to/killrweather  
    c:/path/to/cassandara/bin/cqlsh

### In CQL Shell:
You should see:

     Connected to Test Cluster at 127.0.0.1:9042.
     [cqlsh 5.0.1 | Cassandra 2.1.14 | CQL spec 3.2.1 | Native protocol v3]
     Use HELP for help.
     cqlsh>

Run the scripts, then keep the cql shell open querying once the apps are running:

     cqlsh> source 'create-timeseries.cql';
     cqlsh> source 'load-timeseries.cql';


### Run

#### From Command Line

1) Start `KillrWeather`

    cd /path/to/killrweather
    sbt app/run

As the `KillrWeather` app initializes, you will see Akka Cluster start, Zookeeper and the Kafka servers start.

If you find the KillrWeather app is [unable to connect to Cassandra](https://github.com/killrweather/killrweather/issues/24#issuecomment-144140773) you might try `sbt app/run -Dcassandra.connection.host=127.0.0.1` instead. (At least, that worked for me.)

2) Start the Kafka data feed app
In a second shell run:

    sbt clients/run

You should see:

    Multiple main classes detected, select one to run:

    [1] com.datastax.killrweather.KafkaDataIngestionApp
    [2] com.datastax.killrweather.KillrWeatherClientApp

Select `KafkaDataIngestionApp`, and watch the shells for activity. You can stop the data feed or let it keep running.
After a few seconds you should see data by entering this in the cqlsh shell:

    cqlsh> select * from isd_weather_data.raw_weather_data;

This confirms that data from the ingestion app has published to Kafka, and that raw data is
streaming from Spark to Cassandra from the `KillrWeatherApp`.

    cqlsh> select * from isd_weather_data.daily_aggregate_precip;

Unfortunately the precips are mostly 0 in the samples.

3) Open a third shell and again enter this but select `KillrWeatherClientApp`:

    sbt clients/run

This api client runs queries against the raw and the aggregated data from the kafka stream.
It sends requests (for varying locations and dates/times) and for some, triggers further aggregations
in compute time which are also saved to Cassandra:

* current weather
* daily temperatures
* monthly temperatures
* monthly highs and low temperatures
* daily precipitations
* top-k precipitation

Watch the app and client activity in request response of weather data and aggregation data.
Because the querying of the API triggers even further aggregation of data from the originally
aggregated daily roll ups, you can now see a new tier of temperature and precipitation aggregation:  
In the cql shell:

    cqlsh> select * from isd_weather_data.daily_aggregate_temperature;
    cqlsh> select * from isd_weather_data.daily_aggregate_precip;
