import csv
from math import sin, cos, asin, radians, sqrt

#  
def findDistance(lat1, long1, lat2, long2):
    '''#Finds the distance between two countries, given their latitudes and longitudes'''
    lat1 = radians(lat1)
    long1 = radians(long1)
    lat2 = radians(lat2)
    long2 = radians(long2) 

    return round(7926.2 * max(-1, min(1, asin(sqrt( sin((lat2-lat1)/2)**2 + cos(lat1)*cos(lat2) * sin((long2-long1)/2)**2 )))), 2)

def findAvDist(countryInfo, dataset):
    '''Returrns float of the mean distance of a country to every other country'''
    distances = []
    counter = 0
    for line in dataset:
        if line[0] != countryInfo[0]:
            distances.append(findDistance(float(countryInfo[1]), float(countryInfo[2]), float(line[1]), float(line[2])))
            counter += 1

    return round(sum(distances)/counter, 3)

#Read CSV file
with open("world_country_and_usa_states_latitude_and_longitude_values.csv", 'r') as file:
    reader = csv.reader(file)
    header = next(reader) + ["Average Distance"]
    rows = list(reader)

    #Write to new CSV file
    with open("new.csv", 'w') as new_file:
        writer = csv.writer(new_file, delimiter=",", lineterminator='\n')
        writer.writerow(header)
        for row in rows:
            writer.writerow(row + [findAvDist(row, rows)])
