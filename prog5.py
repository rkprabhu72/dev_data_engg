import mysql.connector
import pandas as pd
db_config = {
    "host": "localhost",        
    "user": "root",      
    "password": "V1chm@$n",  
    "database": "MRTSdb"   
}
query = """
SELECT Year, NAICSCode,AVG(Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct + Nov + December) / 12 AS Adjusted_Annual_Average
FROM MRTS_data_consolidated WHERE NAICSCode = 44611 AND Year BETWEEN 1992 AND 2020 AND Data_type = 'Adjusted'GROUP BY Year, NAICSCode order by Year
;"""
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    result_df = pd.DataFrame(rows, columns=column_names)
    output_file = "/Users/rkprabhu/Downloads/adjusted_annual_averages.csv" 
    result_df.to_csv(output_file, index=False)
    print(f"Query results exported to {output_file}")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
