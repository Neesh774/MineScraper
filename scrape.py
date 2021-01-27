import bs4
from urllib.request import urlopen as uReq, Request
from bs4 import BeautifulSoup as soup
from csv import writer
mineurl = 'https://www.minecraftcrafting.info/'
req = Request(mineurl, headers={'User-Agent': 'Mozilla/5.0'})
page_html = uReq(req).read()
page_soup = soup(page_html, "html.parser")
data = page_soup.findAll("td")
count = -2
t = open("titles.txt", "w")
i = open("ingredients.txt", "w")
u = open("descriptions.txt", "w")
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
        # print("Image: ")
        count += 1
    elif count == 3:
        u.write(str(item.text.strip()) + ':')
        count = 0
t.close()
i.close()
u.close()