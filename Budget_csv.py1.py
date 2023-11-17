import os
import csv

code main.py

budget_csv = os.path.join("..","resources","budget_data.csv" )

with open(csvpath) as CSVfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print ("financial analysis")

months = (list(csvreader))
print ("total months", months + int(1))








