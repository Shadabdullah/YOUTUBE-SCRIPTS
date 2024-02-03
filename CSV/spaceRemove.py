import csv

# Replace 'D:\CODES\YOUTUBE-SCRIPTS\CSV\data.csv' with the path to your CSV file
input_file = 'D:\CODES\YOUTUBE-SCRIPTS\CSV\data.csv'

# Replace 'output.csv' with the desired output file path
output_file = 'output.csv'

# Function to remove extra spaces from a string
def remove_extra_spaces(s):
    return ' '.join(s.split())

# Read input CSV file and write cleaned data to output CSV file
with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        cleaned_row = {key: remove_extra_spaces(value) for key, value in row.items()}
        writer.writerow(cleaned_row)

print("Extra spaces removed from all fields in the CSV file.")
