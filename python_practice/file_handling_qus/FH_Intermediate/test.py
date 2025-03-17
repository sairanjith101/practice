import csv

with open('finance.csv', 'r', newline='') as file1:
    csv_reader = csv.DictReader(file1)

    for row in csv_reader:
        print(row)  # Each row is a dictionary
