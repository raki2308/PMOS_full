import pandas as pd

# Prompt user for the main CSV file name
main_csv = input("Enter the CSV filename: ")

# Read the main CSV file
df_main = pd.read_csv(main_csv)

# Read the CSV to insert (you can also prompt for this if needed)
df_insert = pd.read_csv('header.csv')

# Split main CSV after the first row
df_first = df_main.iloc[:1]
df_rest = df_main.iloc[1:]

# Concatenate: first row + insert + rest
df_result = pd.concat([df_first, df_insert, df_rest], ignore_index=True)

# Overwrite the input CSV file with the result
df_result.to_csv(main_csv, index=False)

