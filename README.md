# Country Distances

This python program generates a csv file with columns: 

- country: name of a country
- latitude: country's latitude
- longitude: country's longitude
- Average Distance: the average distance from the country to every other country

Essentially, it calculates every country's average distance relative to every other country.

## Usage

*(This program is not intended to be used in serious scientific analysis, since it is not proven or reliable)*
This program can be used to understand the density of countries, visualizing which ones are most "dense", and which are most "isolated".

## How It Works

- Reads a CSV file containing countries, their latitudes, and their longitudes
- For each country, use the Haversine formula to sum up the distance to each other country, then divide by the number of countries, resulting in it's "average distance"
- Write the information to a new CSV

## What I Learned

- Reading from a CSV file
- Writing to a CSV file
- The Haversine formula
- Working with large datasets
