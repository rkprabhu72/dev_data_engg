# read a file from folder and insert into database in MySQL, DB already created in MySQL
import pandas as pd
import mysql.connector

filepath = '/Users/rkprabhu/Downloads/masterdf/master_df.csv'
df = pd.read_csv(filepath)
df.fillna(0, inplace=True) 
df.replace("(NA)", 0, inplace=True)
df.replace("(S)", 0, inplace=True)
print (df.head(5))

connection = mysql.connector.connect(
    host="localhost",         
    user="root",              
    password="V1chm@$n",      
    database = "MRTSdb"         
)
cursor = connection.cursor()
table_name = "MRTS_data_consolidated"
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    Year YEAR,
    Data_type VARCHAR(50),
    NAICSCode VARCHAR(255),
    BusinessType VARCHAR(255),
    Jan INT,
    Feb INT,
    Mar INT,
    Apr INT,
    May INT,
    Jun INT,
    Jul INT,
    Aug INT,
    Sep INT,
    Oct INT,
    Nov INT, 
    December INT,
    Total INT
);
"""
cursor.execute(create_table_query)
for index, row in df.iterrows():
    insert_query = f"""
    INSERT INTO {table_name} (Year, Data_type, NAICSCode, BusinessType, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov,December, Total )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(insert_query, tuple(row))

# Commit the transaction and close the connection
connection.commit()
cursor.close()
connection.close()

print(f"Data Inserted Successfully in MySQL '{table_name}'!!!")
print
