import pandas as pd
import mysql.connector

filepath = '/Users/rkprabhu/Downloads/samplecsv.csv'
df = pd.read_csv(filepath)
df.fillna(0, inplace=True) 
print (df.head(2))
connection = mysql.connector.connect(
    host="localhost",         
    user="root",              
    password="V1chm@$n",      
    database = "sampleDB"         
)
cursor = connection.cursor()
table_name = "sampleDB"
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    Year VARCHAR(255),
    Datatype VARCHAR(255),
    NAICSCode VARCHAR(255),
    BusinessType VARCHAR(255),
    Jan VARCHAR(255),
    Feb VARCHAR(255),
    Mar VARCHAR(255),
    Apr VARCHAR(255)
);
"""
cursor.execute(create_table_query)
for index, row in df.iterrows():
    insert_query = f"""
    INSERT INTO {table_name} (Year, Datatype, NAICSCode, BusinessType, Jan, Feb, Mar, Apr)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(insert_query, tuple(row))

# Commit the transaction and close the connection
connection.commit()
cursor.close()
connection.close()

print(f"Data Inserted Successfully '{table_name}'!!!")