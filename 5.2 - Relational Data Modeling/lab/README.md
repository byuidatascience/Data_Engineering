Data Modeling Practice
----------------------

In this exercise, you will demonstrate your understanding of normalization by designing a data model.  By now you know how to use python to extract the data you need and insert it into a database.  The tweets table that we created is in 3NF.  Now we want to add more tables to our database but we want to make sure we follow 3NF.

1. Design a simple data model involving tweets, users, and entities. How many tables do you need? 2? 3? 4? What is the relationship between them? What is the relationship between a tweet and a user (one-to-one, one-to-many, many-to-many)? Similarly, what is the relationship between tweets and entities? What are the primary keys and foreign keys? Draw this out. You may use an [ER](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) diagram, [UML](http://www.agiledata.org/essays/umlDataModelingProfile.html), or something of your own design, so long as it is easy to read and understand. You may use [Graphviz](http://www.graphviz.org/) or pen and paper or a tool like [Gliffy](https://www.gliffy.com/).

2. Create a new tables using pgAdmin for entities and users using the tweet id and user id as your primary keys respectively. Other data that are atomic and functionally dependent on the tweet id should be included such as the `hashtags`, _etc._  *Pop quiz:* why did we include user id instead of screen name in our tweets table?

3. Modify your python code from yesterday to insert data into your new tables.  In the next lab, we'll insert our data using Spark, bringing our database up to date with our data lake.

### Stretch Goal

Using pgAdmin's `query tool`, write SQL code to join your three tables into one.

----

#### On completing this assignment, you should have submitted:

- A visual data model (`.jpg`, `.png`, or `.svg`)
- A python (`.py`) file that inserts data into the two new tables in your database
