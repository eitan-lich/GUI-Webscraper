import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup


website_url = None

def main():
    root = tk.Tk(className="Website scraper")
    root.geometry("700x200")

    website_url_label = tk.Label(root,
        text="Enter the URL of the website you wish to scrape",
        padx=10,
        pady=10,
        font=('Helvetica 15 bold', 18),
        bg='#99CCFF')

    website_url_label.pack()

    website_url = tk.Entry(root,width=50)
    website_url.pack()
    URL = website_url.get()

    button = tk.Button(root, text="Download raw HTML", command=url_find,
                       padx=2,
                       pady=2,
                       font=('Helvetica 15 bold', 10),
                       bg='#FFF')
    button.pack()


    root.mainloop()


def download(html, name):
    with open(f"{name[:5]}.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(html)


def url_find():
    if URL == "":
        messagebox.showwarning("Missing/Invalid URL", "Must enter a valid URL")
        return
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string
    download(soup.prettify(), title)


