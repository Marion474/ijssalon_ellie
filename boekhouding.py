import csv
from presentatie import *
from helper import *

inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes- totaal" : 750
}

print(inkomsten)

mijn_dict = inkomsten
totaal_inkomsten = som(inkomsten)
print(totaal_inkomsten) 


presenteer(inkomsten, totaal_inkomsten)


with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow([key,value])