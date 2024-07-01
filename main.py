import os
import requests

APIKEY=os.environ.get('weatherAPI') #hiding api key in the system environment variable
print(APIKEY) 
location=input("Enter the city Name:")
#api call 
complete_api_link ="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+APIKEY


api_link=requests.get(complete_api_link)
api_data=api_link.json() # getting the json data from the link
#print(api_data)

if api_data['cod']=='404':
    print("some error occured,check your city name".format(location))

else:
    weather_desc=(api_data['weather'][0]['description'])
    temp_city=((api_data['main']['temp'])-273.15)
    humidity_city=(api_data['main']['humidity'])
    windspeed_city=(api_data['wind']['speed'])


print(weather_desc)
print(temp_city)
print('; degree celcius\n')
print(humidity_city)
print('; pascal\n')
print(windspeed_city)
print('; kilometer/hour\n')
