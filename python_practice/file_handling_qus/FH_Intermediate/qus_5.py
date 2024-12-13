# Write a program to read a CSV file and print its content.

import csv

with open('finance.csv') as file1:
    csv_reader = csv.reader(file1)

    for row in csv_reader:
        print(row)