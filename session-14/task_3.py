import csv

file = open("session-14/ipl_matches.csv", "r")
data = csv.DictReader(file)

for match in data:
    print(match["Winner"])

file.close()