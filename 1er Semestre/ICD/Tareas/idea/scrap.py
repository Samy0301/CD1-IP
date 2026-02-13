import requests
from bs4 import BeautifulSoup
import json 

url = "http://www.cubadebate.cu/"
response= requests.get(url)
soup=BeautifulSoup(response.content,"html.parser")

#codigo para crear archivo html de la pagina 
with open('cubadebate.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

lista_titulos=[]
titulos = soup.find_all("div", class_="title")
titulos2=soup.find_all("a", class_="title")
for i in titulos :
    lista_titulos.append(i.text)
for i in titulos2:
    lista_titulos.append(i.text)

for x in lista_titulos:
    print(x)
    
