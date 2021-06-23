import requests
#import os
from datetime import datetime

api_key = '020f0830f5d101b36e84a91783af0d45'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
f=open('weather.txt','a')
f.write("Current temperature is: {:.2f} deg C".format(temp_city))
f.write("Current weather desc :{}".format(weather_desc))
f.write("Current Humidity :{} {} ".format(hmdt,'%') )
f.write("Current wind speed : {} {} ".format(wind_spd,'kmph')  )

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
f.close()