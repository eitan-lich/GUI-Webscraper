import requests
from bs4 import BeautifulSoup
from Gui import Gui

def download(html, name):
    with open(f"{name[:5]}.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(html)

def url_find():
    URL = website_url.get()
    ok = gui()

    if URL == "":
        return
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string
    download(soup.prettify(), title)

def run():
    app = Gui()
    app.window()
    url = app.setup_window()
    app.run()

