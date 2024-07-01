# to download image using the image url
import requests
r=requests.get('https://cloud-f4lij7sq1-hack-club-bot.vercel.app/0flowerpcb.png')

with open("imageName.png",'wb') as f:
    f.write(r.content)
