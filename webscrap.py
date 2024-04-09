import psycopg2

connection = psycopg2.connect(user ="pgadmin4",
pasword="admin",host="localhost",port="5050",database = "TestDataBase")

cursor = connection.cursor()