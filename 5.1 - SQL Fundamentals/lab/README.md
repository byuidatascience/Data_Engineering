Squashing Birds
---------------

I was going to call it "Flattening Tweets" but decided to make it more gruesome.

As you've seen, SQL places some restrictions on the kind of data we can put into it. Later we will go into what it means for data to be "normalized" but for now we can focus on what's called the First Normal Form, or [1NF](https://en.wikipedia.org/wiki/First_normal_form) which requires that each piece of data be atomic. That means no arrays and that means no nested data. If we are going to put our Twitter data into a SQL database, we will need to address this problem.

### Getting Started with Amazon RDS

For today's lab, start by [Creating a PostgreSQL DB Instance and Connecting to a Database on a PostgreSQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html). (To stay on the [free tier](https://aws.amazon.com/rds/free/), you'll want to do a Single-AZ deployment on a db.t2.micro instance with no more than 20 GB storage.)

**Important:** Be sure to use Postgres 9.6 or later. (At the time of this writing, RDS still defaults to 9.5, though 9.6 is available.)

Note: the screenshots under [Using pgAdmin to Connect to a PostgreSQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html#CHAP_GettingStarted.Connecting.PostgreSQL) are still based on pgAdmin 3. We will be using pgAdmin 4 which is slightly different but should follow the same principles.  You will likely want use [this download link](https://www.postgresql.org/download/macosx/).

#### DDL

There are two parts of the Structured Query Language: the data definition language (DDL) and the data manipulation language (DML). Most of the time we are focused on the DML which provides us with the CRUD operations: INSERT, SELECT, UPDATE, DELETE, before we do any of that, we need a data model to manipulate. Postgres and other RDBMSs require you to CREATE your tables before you put anything into them. For today's lab, we will keep it simple.

To begin with, there is a lot of data we don't need. Since we are already storing all of our raw data in S3, we can safely disregard the majority of it. (We can always add it later if we need it.) So let's focus on what we need. We'll start with the same problem we've been using Hadoop and Spark for: calculating the frequency of hashtags. For this we will want a table called `hashtags` that contains two columns: `id` and `hashtag`. To do this using [pgAdmin](https://www.pgadmin.org/docs4/1.x/index.html):

1. Connect to your RDBMS. The easiest way to do this is to click "Add New Server" under "Quick Links".
    1. Name it whatever you want (I pick the same name I used in AWS for simplicity).
    2. Go to the "Connection" tab
    3. Enter the Host address. This is the URL provided by AWS which should be [your database name].[some hash].[your region (_i.e._`us-east-1`)].`rds.amazonaws.com`. This appears as your "endpoint" (not including `:5432`) in your RDS configuration detailed-schedule
    4. Leave the port (5432) and maintenance database (postgres) alone
    5. Fill in the user name and password you specified when launching your database. You may (if you wish) save your password.
    6. You may ignore Role and SSL mode for now.
    7. Save.
2. Create your table
    - You'll now see your RDS server on the left under Servers. Expand it.
        - You'll now see Databases, Login/Group Roles, and Tablespaces under your server. Click "Databases"
            - You'll now see your database along with a maintenance database, which you can ignore.  Click on the one you created in AWS.
                - You'll now see Casts, Catalogs, Event Triggers, Extensions, Foreign Data Wrappers, Languages, and Schemas. These are all advanced topics to be covered on your own at a later date. For now, click "Schemas"
                    - For now, there should just be one Schema: "public". Expand it.
                        - Now we have Collations, Domains, _etc. &c._
                        - Right click on "Tables" and select Create -> Table...
                            1. Name your table `tweets`
                            2. Leave Owner, Schema, and Tablespace default and go to the "Columns" tab
                            3. Hit the "+" on the right to create a new column
                                1. Name: `tweet_id`
                                2. Data type: `bigint`
                                3. Length and Precision do not apply to `bigint` data.
                            4. Hit the "+" on the right to create a new column
                                1. Name: `text`
                                2. Data type: `character varying`
                                3. Length: `200`
                            5. Set Not NULL? and Primary key? to "Yes" for both columns.
                            6. Create new columns for `user_id`, `timestamp_ms`, `created_at`, `lang`, `possibly_sensitive` too.  Choose the best data type and lengths for these columns noting some of your tweets might be missing these values

### Building a squashed bird pipeline with psycopg2

[`psycopg2` is a library](http://initd.org/psycopg/docs/) designed for interacting with Postgres databases from python (similar to how `boto` allows us to interact with AWS).  You can install it using `pip install psycopg2`.  To use this library, you must define a connection and a cursor.  A basic workflow would look something like this.  **Do not copy and paste this.  Type this out yourself to help you think through the problem, especially how your solution will differ from this starter code**:

        from os.path import expanduser
        import psycopg2
        import yaml

        credentials = yaml.load(open(expanduser('~/api_cred.yml')))

        conn = psycopg2.connect(**credentials['rds'])  # connect to postgres
        cur = conn.cursor()  # create a cursor
        count = 0
        for datum in my_data:
            count += 1
            cur.execute("INSERT INTO my_table (column1, column2, column3) VALUES (%s, %s, %s)", (datum[0], datum[1], datum[2]))  # insert data into three columns
            if count > 100:
                conn.commit()  # commit insertions
                count = 0
        conn.commit()  # make sure all data has been committed
        conn.close()  # close the connection

Once your database has been created and your data model defined, you will need to populate your database. You should have one row for every tweet. **Develop this first using a sample file from S3 as we did before. Tomorrow we will scale it up using Spark, so leave your database running.**

Don't forget to [`commit`](http://initd.org/psycopg/docs/connection.html#connection.commit) your transaction after your insert. You may commit after every insert or, to save time, you may want to commit after every 100 or so inserts.  You can also find [more information here](http://initd.org/psycopg/docs/usage.html).

### Stretch Goal

Now that you've gotten a sense for how to create a table through the GUI (graphic user interface), spend some time exploring pgAdmin to see the different functionality of a Postgres database that you might not be familiar with.  Think about how you would do these same tasks programatically at the command line instead of through the GUI.  Create a list that compares the two approaches for common tasks.

----

#### On completing this assignment, you should have submitted:

- A script (`.py`) that INSERTs hashtags into a PostgreSQL database
