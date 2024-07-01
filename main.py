import os
import requests

APIKEY=os.environ.get('weatherAPI') #hiding api key in the system environment variable
print(APIKEY) 
location=input("Enter the city Name:")
#api call 
complete_api_link ="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+APIKEY


api_link=requests.get(complete_api_link)
api_data=api_link.json() # getting the json data from the link
print(api_data) # printing the whole json object

