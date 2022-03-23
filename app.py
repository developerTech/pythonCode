import psycopg2

connection = psycopg2.connect('dbname=udacity')
cursor = connection.cursor()

"""
cursor.execute('''
    CREATE TABLE test (
        id INTEGER PRIMARY KEY,
        task BOOLEAN NOT NULL DEFAULT FALSE
    );
''')
"""

# cursor.execute('INSERT INTO test (id, task) VALUES (1, true);')

# cursor.execute('INSERT INTO test (id, task) VALUES (%s, %s);', (2, False))
'''
data = {
    'id': 3,
    'task': True
}
sql = 'INSERT INTO test (id, task) VALUES (%(id)s,%(task)s);'
cursor.execute(sql,data)
'''

cursor.execute("SELECT * FROM test")
#result= cursor.fetchall()
#print(result)


result1= cursor.fetchmany(2)
print(result1)

connection.commit()
connection.close()
cursor.close()