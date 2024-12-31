import mysql.connector
import pandas as pd
db_config = {
    "host": "localhost",        
    "user": "root",      
    "password": "V1chm@$n",  
    "database": "MRTSdb"   
}
query = """
select Year, Total from MRTS_data_consolidated where BusinessType = 'Food and beverage stores' and Data_type = 'Unadjusted' AND Year BETWEEN 1992 AND 2020 order by Year Desc;"""
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    result_df = pd.DataFrame(rows, columns=column_names)
    print(result_df.head())
    output_file = "/Users/rkprabhu/Downloads/Food_BeverageStores.csv" 
    result_df.to_csv(output_file, index=False)
    print(f"Query results exported to {output_file}")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
