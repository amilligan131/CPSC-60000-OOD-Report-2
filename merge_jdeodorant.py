import csv

# Read the classes with smells from the JDeodorant .txt file
with open(r'C:\Users\drewm\Downloads\junit4-god class bad smells.txt', 'r') as f:
    classes_with_smells = {line.split('\t')[0].strip() for line in f}

# Open the CK .csv file and a new .csv file to write the output
with open(r'C:\Users\drewm\Downloads\junit4-metrics.csv', 'r') as f_in, open(r'C:\Users\drewm\Downloads\junit4-metrics-CLEANED.csv', 'w', newline='') as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)

    # Write the header row to the new .csv file
    header = next(reader)
    header.append('smell')
    writer.writerow(header)

    # Process each row in the CK .csv file
    for row in reader:
        # Add a column that indicates whether the class has a smell
        classname = row[0]  # Assumes class name is in first column
        row.append('yes' if classname in classes_with_smells else 'no')

        # Write the row to the new .csv file
        writer.writerow(row)