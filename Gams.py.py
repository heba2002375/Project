import bs4
from bs4 import BeautifulSoup
import requests
url='https://play.google.com/store/games'
page= requests.get(url)
 soup=BeautifulSoup( page.content,"html.parser")
Gam_name= soup.find_all("span",{"class","sT93pb DdYX5 OnEJge "})
gameRate=soup.find_all("span",{"class","w2kbF"})
for i in range(len(Gam_name)):
    print(Gam_name[i].text)
    print(gameRate[i].text)

