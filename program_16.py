# 16. Import and export data between pandas and MySQL database
import pandas as pd
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="school"
)

# Import data from MySQL into pandas
df = pd.read_sql("SELECT * FROM students", conn)
print("Data from MySQL:")
print(df)

# Export a DataFrame back to MySQL
df.to_sql('students_copy', con=conn, if_exists='replace', index=False)

conn.close()
