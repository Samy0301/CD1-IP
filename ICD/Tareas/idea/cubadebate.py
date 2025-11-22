#Sin VPN da error la solicitud a cubadebate
from bs4 import BeautifulSoup
import requests

web = requests.get("http://www.cubadebate.cu/")

if web.status_code == 200:

    soup = BeautifulSoup(web.text, 'html.parser')

    div_title = soup.find_all("div",attrs={"class":"title"})

    titles = [i.text for i in div_title]

    for i in titles:
        print(f"- {i}")
        
else:
    print("Error al realizar la solicitud")