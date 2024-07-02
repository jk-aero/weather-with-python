import os
import pygame,sys
import requests

APIKEY=os.environ.get('weatherAPI') 
location=''
weather_desc=''
temp=None
humidity=None
windspeed=None

#api call 
def getData():
    complete_api_link =f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={APIKEY}"
    api_link=requests.get(complete_api_link)
    api_data=api_link.json()
    #print(api_data)
    global weather_desc
    weather_desc=api_data['weather'][0]['description']
    temp=(api_data['main']['temp'])-273.15
    humidity=api_data['main']['humidity']
    #date_time=date_time.now().strftime("%d %b %Y")

    
 



 
# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Text Rendering Example")



# Load a font
base_font = pygame.font.Font(None, 32)
Title_font = pygame.font.Font(None, 42)
subTitle_font = pygame.font.Font(None, 20)
heading_text="welcome to weather app"
subHeading="please enter your city name \nand  press enter to know \ncurrent weather at your location"
user_text=''

#Rect
InputRect=pygame.Rect(60,100,250,32)#x,y width,height
ButtonRect=pygame.Rect(65,160,100,45)


# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
Color_active=pygame.Color('lightskyblue3')
Color_passive=pygame.Color('gray15')
Color=Color_passive
active=False
btn_color=Color
textbx_color=Color

# Main loop
while True:

    mousePose=pygame.mouse.get_pos()
    
   # print(mousePose)...........................
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
    




    #handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if active ==1:
            #handling backapace 
            if event.type == pygame.KEYDOWN:           
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ButtonRect.collidepoint(event.pos):
                if user_text:  
                    location=user_text
                    print(location)
                    getData()
                
           








    
    # Clear the screen
    screen.fill(WHITE)  
    pygame.draw.rect(screen,textbx_color,InputRect,3)
    pygame.draw.rect(screen,btn_color,ButtonRect)

    # Render text
    text_surface = base_font.render(user_text, True, BLACK)
    text_surface1 = Title_font.render(heading_text, True, BLACK)
    text_surface2 = subTitle_font.render(subHeading, True, BLACK)
    text_surface3 = subTitle_font.render("ENTER", True, WHITE)
    weatherDes_surface = base_font.render(f"{weather_desc}", True, BLACK)

    screen.blit(text_surface1, (60, 30))
    screen.blit(text_surface2, (250, 160))
    screen.blit(text_surface, (InputRect.x+10, InputRect.y+5))
    screen.blit(text_surface3, (ButtonRect.x+10, ButtonRect.y+13))
    screen.blit(weatherDes_surface, (50, 230))

    #input text dynamic width
    InputRect.width=max(250,text_surface.get_width()+15)

    # Update the display
    pygame.display.flip()
