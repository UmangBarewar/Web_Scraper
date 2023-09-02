import requests
from bs4 import BeautifulSoup

with open("Sample.html","r") as f:
    html_doc = f.read()

soup=BeautifulSoup(html_doc,'html.parser')
# print(soup.prettify())
# print(soup.title.string,type(soup.title.string))
# print(soup.find_all("div")[2])
for link in soup.find_all("a"):
    # print(link.get("href"))
    # print(link)
    # print(link.get_text())
    # print(soup.select("span#oye"))
    # print(soup.select("div.Lucifer"))
    print(soup.find(class_="Lucifer"))