#! python3
# UmbrellaReminder.py - Scrapes weather.gov and reminds the user to bring an umbrella if there is a chance of rain

import requests, bs4, json

def main():
    locationFile = open('location.json', 'r')
    locationString = locationFile.read()
    locationFile.close()
    locationURL = json.loads(locationString)['locationURL']
    checkWeather(locationURL)

def checkWeather(url):
    # Create request for url
    req = requests.get(url)
    req.raise_for_status()
    # Parse the html
    soup = bs4.BeautifulSoup(req.text, 'html.parser')
    # Check today's weather description
    weatherDescription = soup.select('div.row-odd:nth-child(1) > div:nth-child(2)')
    if weatherDescription == []:
        print("Unable to find today's weather description")
        return

    descriptionList = weatherDescription[0].getText().split()
    
    # Check if the list contains the word showers, rain, precipitation
    if 'showers' in descriptionList or 'precipitation' in descriptionList or 'rain' in descriptionList:
        print('There is a chance of rain! Bring an umbrella!')

if __name__ == '__main__':
    main()