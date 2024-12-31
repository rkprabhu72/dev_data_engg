import pandas as pd

import os


inputfile = '/Users/rkprabhu/Downloads/mrtssales92-present(3).xls'  

# Read all sheets into a dictionary
inputdata = pd.read_excel(inputfile, sheet_name=None, header=None)

# Create a directory in Google Drive to save CSV files
outputdir = '/Users/rkprabhu/Downloads/csvs_14'
os.makedirs(outputdir, exist_ok=True)

# Process each worksheet
for sheet_name, df in inputdata.items():
    # Step 3: Delete first 4 rows, row 6, row 72, and rows after 110
    #df = df.drop(index=list(range(4)))  # Drop the first 4 rows
    df = df.drop(index=[0,1,2,3,4,5,71])  # Drop row 7 (index 6) and row 72 (index 71)
    df = df[df.index < 109]  # Keep rows up to 110 (index 109)
    new_column_names = ["NAICSCode", "BusinessType", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "December", "Total"]
    num_columns = len(df.columns)  # Get the number of existing columns in the DataFrame
    for i in range(num_columns):
        df.rename(columns={df.columns[i]: new_column_names[i]}, inplace=True)
    # Step 4: Insert 'Year' column with the sheet name
    df.insert(0, 'Year', sheet_name)

    # Step 5: Insert 'Data_type' column
    df.insert(1, 'Data_type', 'Unadjusted')  # Insert column with default value "Unadjusted"
    df.loc[df.index > 70, 'Data_type'] = 'Adjusted'  # Update rows after index 64 to "Adjusted"
    
    # Step 6: Write the modified DataFrame to a CSV file in Google Drive
    outputfile = os.path.join(outputdir, f'{sheet_name}.csv')
    df.to_csv(outputfile, index=False)
    print(f"Processed and saved sheet: {sheet_name} as {outputfile}")