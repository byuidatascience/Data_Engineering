Advanced Querying
---------

Time for some [SQL Katas](https://en.wikipedia.org/wiki/Kata_(programming))!  In the past few labs you have created a relational database with at least three tables.  You can run SQL queries on your database using pgAdmin's query tool.  SQL is unlike programming paradigms like OOP and functional in that it's a declarative language.  To use SQL, you declare the result that you want your database to return.  This is a fascinating language as it allows you to return complex queries with a limited vocabulary.

Now that we have a populated database, let's see what we can do with it.  Create a markdown (`.md`) document to record **both the query and the result** for the following questions.  Copy and paste the questions in this new markdown document.

### Basic Operations

Explore each of these tables using `SELECT * FROM <table_name> LIMIT 5` to make sure the tables are what you'd expect.  If you get stuck, check out [this website](https://www.w3schools.com/sql/).

1. How many rows are in the entities table?

2. How many distinct users are in your database?

3. When was the oldest tweet in your database?

### Filtering Records

4. How many possibly sensitive tweets are in your database?

5. How many tweets are in your database from between Tuesday and Thursday of last week?  If this is not in your dataset for some reason, you can change the dates to encompass a few days of activity.

6. What are the top 5 hashtags and their counts?  When you return the two columns, rename the hashtag column `top_hashtags` and the counts `hashtag_count`

7. What is the average time that each language was tweeting on a day of your choosing last week?  Limit this query to five rows.

### Joins and Cases

Take a look at the different kinds of [joins here.](https://www.w3schools.com/sql/sql_join.asp)  Also note that `CASE WHEN` is SQL's if/else control structure; this is particularly helpful in dealing with null values.

8. Return the first 5 rows of a table that has two columns, one for your tweet text and the other for the user screen name (you'll have to join your tweets and user table for this).

9. Return the first 5 rows of a table with three columns: your tweet text, screen name, and hashtags.

10. Return ten rows of a table that has two columns: `tweet_text` and `language`.  This should only include English and Japanese tweets.  Use `CASE WHEN` to replace `en` with `English` and `ja` with `Japanese`.

**Save the markdown file you created in a convenient place.  This lab is designed to give you a roadmap through SQL queries in the future**

### Stretch Goal

Create a list of the top 20 hashtags as before, but this time there should be two new columns:

1. the timestamp of the first tweet that had that hashtag
2. the screen name of the user that sent that tweet

You may find it useful to create one or two temporary views on the way to this final goal.

----

#### On completing this assignment, you should have submitted:

- A markdown file with your queries and results
