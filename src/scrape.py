import requests
from bs4 import BeautifulSoup
from src.Gui import Gui

def download(html, name):
    with open(f"{name[:5]}.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(html)

def url_find():
    ok = Gui()
    response = "<!DOCTYPE HTML><html><head></head><body><h1>test</h1></body></html"
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string
    download(soup.prettify(), title)

def run():
    app = Gui()
