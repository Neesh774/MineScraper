import bs4
from urllib.request import urlopen as uReq, Request
from bs4 import BeautifulSoup as soup
from csv import writer
import requests
import os.path

mineurl = 'https://www.minecraftcrafting.info/'
req = Request(mineurl, headers={'User-Agent': 'Mozilla/5.0'})
page_html = uReq(req).read()
page_soup = soup(page_html, "html.parser")
data = page_soup.findAll("td")
count = -2
t = open("titles.txt", "w")
i = open("ingredients.txt", "w")
u = open("descriptions.txt", "w")
data.pop(0)
data.pop(1)
data.pop(2)
data.pop(3)
for item in data:
    if count<0:
        count += 1
    elif count == 0:
        t.write(str(item.text.strip()) + ':')
        count += 1
    elif count == 1:
        i.write(str(item.text.strip()) + ':')
        count += 1
    elif count == 2:
        count += 1
    elif count == 3:
        u.write(str(item.text.strip()) + ':')
        count = 0
t.close()
i.close()
u.close()
image = soup(page_html, "html.parser")
images = image.find_all('img') 
images.pop(0)
for item in images: 
    response = requests.get(mineurl+item['src'])
    filename = item['src'].split('/')[-1]
    save_path = "C:/Users/rkanc/MineScraper/images"
    completeName = os.path.join(save_path, filename)
    file = open(completeName, "wb")
    file.write(response.content)
    file.close()
    #  print(mineurl + item['src'])