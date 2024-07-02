import os
import requests
import pygame 

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


  
# Define the background colour 
background_colour = (50, 50, 50) 
  
# Define the dimensions of screen object(width,height) 
screen = pygame.display.set_mode((600, 450)) 
  
# Set the caption of the screen 
pygame.display.set_caption('weather app') 
  
# Fill the background colour to the screen 
screen.fill(background_colour) 
  

  
# Variable to keep our game loop running 
running = True
button = pygame.Rect(100, 200, 90, 70) 
text = pygame.Rect(70, 150, 400, 40) 
Color1=(150,68,98)

Color2=(200,200,200)

# game loop 
while running: 
    mousePose=pygame.mouse.get_pos()
    if button.collidepoint(mousePose):
        Color1=(150,95,98)
    else:
       Color1=(150,68,98)


    if text.collidepoint(mousePose):
        Color2=(255,255,255)
    else:
       Color2=(200,200,200)


    pygame.draw.rect(screen, Color1, button)  # Corrected line
    pygame.draw.rect(screen, Color2, text)  # Corrected line
    pygame.display.flip() # Update the display using flip 
  
    # for loop through the event queue   
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

# End of game loop
pygame.quit()
