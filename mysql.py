import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
        user='user',
        password='password',
        host='localhost',
        database='database'
    )
cursor = cnx.cursor()

# Create the table
table_name = 'stock_data'
query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, date DATE, company VARCHAR(255), close FLOAT, volume INT)"
cursor.execute(query)

# Insert data into the table
def insert_data(date, company, close, volume):
    query = "INSERT INTO stock_data (date, company, close, volume) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (date, company, close, volume))
    cnx.commit()

# Update data in the table
def update_data(date, company, close, volume):
    query = "UPDATE stock_data SET close=%s, volume=%s WHERE date=%s AND company=%s"
    cursor.execute(query, (close, volume, date, company))
    cnx.commit()

# Close the connection
cnx.close()

