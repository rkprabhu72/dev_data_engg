import pandas as pd
import mysql.connector


db_config = {
    "host": "localhost",        
    "user": "root",      
    "password": "V1chm@$n",  
    "database": "MRTSdb"   
}
query = """
select Year, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, December from MRTS_data_consolidated where NAICSCode = 45111 and Data_type = 'Unadjusted' AND Year BETWEEN 1992 AND 2020 order by Year ;"""
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    result_df = pd.DataFrame(rows, columns=column_names)

    
    
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
result_df.rename(columns={'December': 'Dec', }, inplace=True)
print(result_df.head())
df_melted = pd.melt(result_df, id_vars=["Year"], var_name="Month", value_name="Value")
df_melted["YearMonth"] = df_melted["Month"] + "-" + df_melted["Year"].astype(str)
df_pruned1 = df_melted.drop('Month', axis=1)
df_pruned  = df_pruned1.drop('Year', axis=1)
df_pruned.rename(columns = {'Value':'SportStores'}, inplace=True)
print(df_pruned.head())
output_file = "/Users/rkprabhu/Downloads/SportStores10.csv" 
df_pruned.to_csv(output_file, index=False)

print(f"Query results exported to {output_file}")