import os,sys
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


  



# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Text Rendering Example")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load a font
base_font = pygame.font.Font(None, 32)
Title_font = pygame.font.Font(None, 42)
subTitle_font = pygame.font.Font(None, 20)
heading_text="welcome to weather app"
subHeading="please enter your city name \nand  press enter to know \ncurrent weather at your location"
user_text=''

#Rect
InputRect=pygame.Rect(60,100,250,32)
#                      x,y width,height
ButtonRect=pygame.Rect(65,160,100,45)


Color_active=pygame.Color('lightskyblue3')
Color_passive=pygame.Color('gray15')
Color=Color_passive
active=False
btn_color=Color
textbx_color=Color
# Main loop
while True:

    mousePose=pygame.mouse.get_pos()
   # print(mousePose)
    if InputRect.collidepoint(mousePose):
        active=True
        textbx_color=Color_active
    else:
        active=False
        textbx_color=Color_passive

    if ButtonRect.collidepoint(mousePose):
        btn_color=Color_active
    else:
       btn_color=Color_passive
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if active ==1:
            
            if event.type == pygame.KEYDOWN:           
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
    
    # Clear the screen
    screen.fill(WHITE)
    
    pygame.draw.rect(screen,textbx_color,InputRect,3)
    pygame.draw.rect(screen,btn_color,ButtonRect)

    # Render text
    text_surface = base_font.render(user_text, True, BLACK)
    text_surface1 = Title_font.render(heading_text, True, BLACK)
    text_surface2 = subTitle_font.render(subHeading, True, BLACK)
    text_surface3 = subTitle_font.render("ENTER", True, WHITE)

    screen.blit(text_surface1, (60, 30))
    screen.blit(text_surface2, (350, 160))
    screen.blit(text_surface, (InputRect.x+10, InputRect.y+5))
    screen.blit(text_surface3, (ButtonRect.x+10, ButtonRect.y+13))

    #input text dynamic width
    InputRect.width=max(250,text_surface.get_width()+15)

    # Update the display
    pygame.display.flip()
