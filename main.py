import bs4
from bs4 import BeautifulSoup
import requests
url='https://2b.com.eg/ar/computers/laptops.html'
page= requests.get(url)
# print(page.content)
soup=bs4.BeautifulSoup(page.content ,"html.parser")
laptop_name= soup.find_all("a",{"class":"product-item-link"})
price=soup.find_all("span",{"class":"price"})
for i in range(len(laptop_name)):
  print(laptop_name[i].text)
  print(price[i].text)