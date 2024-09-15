import psycopg2

# Connect to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="123456",
    port=5432
)

# Create a new database if it doesn't exist
db_name = "iitdhdb"
conn.autocommit = True  # Set autocommit to avoid running CREATE DATABASE inside a transaction
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE {db_name} ENCODING 'UTF8'")

# Close the cursor and the connection
cursor.close()
conn.close()

