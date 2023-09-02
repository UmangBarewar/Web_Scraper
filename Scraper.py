from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

proxies = {
  'http': '143.110.232.177',
    'https':'89.187.185.244',
}

url = "https://www.amazon.in/Smartphones-Motorola-Basic-Mobiles/s?rh=n%3A1805560031%2Cp_89%3AMotorola"
try:
    ua = UserAgent()
    headers = {'User-Agent': str(ua.chrome)}

    r = requests.get(url,headers=headers)  
    soup = BeautifulSoup(r.text,'html.parser')
    # print(soup.prettify)
    print(soup.select("div#nav-upnav"))
except Exception as e:
    print(f"An error occurred: {e}")


