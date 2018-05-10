import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

class Database:
	def __init__(self):
		self.connect()

	def connect(self):
		self.connection = psycopg2.connect(DATABASE_URL, sslmode='require')
		self.cursor = self.connection.cursor()

	def query(self, query):
		self.cursor.execute(query)
		rows = self.cursor.fetchall()
		return rows

	def insert(self, table_name, data):
		keys = []
		values = []
		for column_name, value in data.items():
			keys.append(column_name)
			values.append(value)
		value_list = "'" + "','".join(str(x) for x in values) + "'"
		query = "insert into " + table_name + " (" + ",".join(keys) + ") values (" + value_list + ")"
		result = self.cursor.execute(query, data)
		self.connection.commit()
