#Write a Python program to read each row from a given csv file and print a list of strings.



import csv

filename = "data.csv"

with open(filename, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)