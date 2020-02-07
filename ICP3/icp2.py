from bs4 import BeautifulSoup
import requests

def wiki_scrap():
    html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
    soup = BeautifulSoup(html.content, "html.parser")
    print("Title of the web page is ", soup.title.string)
    for r in soup.find_all('a'):
        print(r.get('href'))
wiki_scrap()

