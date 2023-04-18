import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost", port="5432")


# Connect to PostgreSQL database
conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost", port="5432")

# Create a table
cur = conn.cursor()
cur.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")
conn.commit()


# Connect to PostgreSQL database
conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost", port="5432")

# Insert data into a table
cur = conn.cursor()
cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("John Doe", "john.doe@example.com"))
conn.commit()

# Connect to PostgreSQL database
conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost", port="5432")

# Insert data into a table
cur = conn.cursor()
cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("John Doe", "john.doe@example.com"))
conn.commit()


# Connect to PostgreSQL database
conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost", port="5432")

# Update a record in a table
cur = conn.cursor()
cur.execute("UPDATE users SET email = %s WHERE name = %s", ("jane.doe@example.com", "Jane Doe"))
conn.commit()


# Connect to PostgreSQL database
conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost", port="5432")

# Update a record in a table
cur = conn.cursor()
cur.execute("UPDATE users SET email = %s WHERE name = %s", ("jane.doe@example.com", "Jane Doe"))
conn.commit()


# Connect to PostgreSQL database
conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost", port="5432")

# Query data from a table
cur = conn.cursor()
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)


# Connect to PostgreSQL database
conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost", port="5432")

# Query data from a table
cur = conn.cursor()
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)
