import csv 
import datetime
import json
import requests
import xmltodict

# Create an array to store each piece of data
mag = []
occured_time = []
lat = []
long = []
state = []
county = []

# Create a function to parse the XML data and append to coresponding array above
def earthquake_data():
    response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")
    if response:
        data = json.loads(response.content)

        """Drill down features in the XML response"""
        features = data["features"]

        """loop through the drill down and extract the data"""
        for feature in features:
            properties = feature["properties"]
            magnitude = properties["mag"]
            mag.append(magnitude)
            time = properties["time"]
            occured_time.append(time)

            """Drill down to gemoetry from the features and extract the data"""
            geometry = feature["geometry"]
            coordinates = geometry["coordinates"]
            latitude = coordinates[1]
            lat.append(latitude)
            longitude = coordinates[0]
            long.append(longitude)
    else:
        return "Connection error, please try again"

# Create a function to convert the timestamps
def time_convert(times):
    timestamps = []
    for i in times:
        i = i // 1000
        datetime_timestamp = datetime.datetime.utcfromtimestamp(i)
        datetime_adj_timestamp = datetime_timestamp - datetime.timedelta(hours=7)
        time_str = datetime_adj_timestamp.strftime("%B %d, %Y at %I:%M:%S %p")
        timestamps.append(time_str)
    return timestamps

# Create a function to get the county and state data from OpenCage Geocoding API using lat and long
def location(lat, long):
    response = requests.get(f'https://api.opencagedata.com/geocode/v1/xml?q={lat}+{long}&key=5346522e59774257aa6ed9fc7d5a2ed8')
    if response:
        data = xmltodict.parse(response.text)
        try:
            country_data = data['response']['results']['result']['components']['county']
            county.append(country_data)
        except:
            county.append("N/A")
        try:
            state_data = data['response']['results']['result']['components']['state']
            state.append(state_data)
        except:
            state.append("N/A")
        return data
    else:
        print("connection error, please try again")

earthquake_data()
timestamps = time_convert(occured_time)

count = 0

# Create a loop that will call the location function x times where x = the number of coordinates in lat
while count < len((lat)):
    location(lat[count], long[count])
    print(f'Magnitude {mag[count]} earthquake on {timestamps[count]} and located at {lat[count]},{long[count]} ' \
        f'in {county[count]}, {state[count]}.')
    count +=1

# Create the headers and organize their data by row for a CSV file
csv_data = [timestamps, mag, lat, long, county, state]
column_data = map(list, zip(*csv_data))

# Open and append the data to a CSV file 
with open("earthquakes.csv", "w", newline='') as file:
    writer = csv.writer(file, lineterminator='\n')

    header = ['Time', 'Magnitude', 'Latitude', 'Longitude', 'County', 'State']
    writer.writerow(header)

    for row in column_data:
        writer.writerow(row)











