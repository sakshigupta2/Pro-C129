import csv
import pandas as pd 
dataset1 = []
dataset2 = []
with open("bright_stars.csv","r",encoding="utf8") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
with open("dwarf_stars.csv","r",encoding="utf8") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)
headers = dataset1[0]
planet_data = dataset1[1:]
headers1 = dataset2[0]
planet_data1 = dataset2[1:]
headersfinal = headers + headers1
planet_data2 = []
for i in planet_data:
    planet_data2.append(i)
for j in planet_data1:
    planet_data2.append(j)

with open("total_stars.csv","w",encoding="utf8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headersfinal)
    csvwriter.writerows(planet_data2)
df = pd.read_csv("total_stars.csv")
df.tail(8)