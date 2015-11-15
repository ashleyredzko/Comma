import sqlite3
from decimal import *

database_connection = sqlite3.connect('comma_database.db')

cursor = database_connection.cursor()
filename = input('Please input the filename: ')
moviename = filename.split('.')
file = open("parseable/" + filename, "r")
row_data = {'name': moviename[0]}

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