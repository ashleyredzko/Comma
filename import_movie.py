import sqlite3
from decimal import *
import os

database_connection = sqlite3.connect('comma_database.db')

cursor = database_connection.cursor()

cursor.execute('CREATE TABLE actors (id integer PRRIMARY KEY, last_name varchar(255), first_name varchar(255))')

cursor.execute('CREATE TABLE movie_actors (id integer PRIMARY KEY, movie_id integer, actor_id integer)')

cursor.execute('CREATE TABLE movies (id integers PRIMARY KEY, name varchar(255), happiness_amt DECIMAL, surprise_amt DECIMAL,sadness_amt DECIMAL, disgust_amt DECIMAL, contempt_amt DECIMAL, neutral_amt DECIMAL, anger_amt DECIMAL, fear_amt DECIMAL)')

files = os.listdir('parseable/')

for filename in files:
	moviename = filename.split('.')
	file = open("parseable/%s" % filename, "r")
	row_data = {
		'name': moviename[0],
	}

	for line in file:
		tokenized_list = line.split(' ')
		row_data[tokenized_list[0]  + '_amt'] = tokenized_list[2].rstrip('\n')

	columns = ', '.join(row_data.keys())
	placeholders = ', '.join('?' * len(row_data))

	sql = 'INSERT INTO movies ({}) VALUES ({})'.format(columns, placeholders)
	print(sql, list(row_data.values()))

	cursor.execute(sql, list(row_data.values()))

database_connection.commit()
database_connection.close()