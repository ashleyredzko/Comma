# Comma

## Create Database
SQLlite version 3.9

```
CREATE TABLE actors (id integer PRRIMARY KEY, last_name varchar(255), first_name varchar(255) );

CREATE TABLE movie_actors (id integer PRIMARY KEY, movie_id integer, actor_id integer );

CREATE TABLE movies (id integers PRIMARY KEY, name varchar(255), happiness_amt DECIMAL, surprise_amt DECIMAL,sadness_amt DECIMAL, disgust_amt DECIMAL, contempt_amt DECIMAL, neutral_amt DECIMAL, anger_amt DECIMAL, fear_amt DECIMAL);
```
