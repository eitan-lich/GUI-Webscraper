import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
import requests
from bs4 import BeautifulSoup

def create(html, name):
    with open(f"{name}.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(html)

def url_find():
    URL = url.get()
    if URL == "":
        messagebox.showwarning("Missing/Invalid URL", "Must enter a valid URL")
        return
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string
    create(soup.prettify(), title)


root = tk.Tk()
root.title("GUI Webscraper")
root.geometry("500x250")

website_url_label = Label(root, text="Website URL:")
website_url_label.pack()

url = tk.StringVar()
website_url = Entry(root,textvariable=url, width=50)
website_url.pack()

URL = website_url.get()

full_html = tk.StringVar()
cb_full_html = Checkbutton(root, text="Full HTML",variable=full_html, onvalue="Full HTML added", offvalue="Full HTML removed")
cb_full_html.pack()

anchor_tags = tk.StringVar()
cb_a_tags = Checkbutton(root, text="Anchor tags",variable=anchor_tags, onvalue="Anchor tags added", offvalue="Anchor tags removed")
cb_a_tags.pack()

images = tk.StringVar()
cb_images = Checkbutton(root, text="Images", variable=images, onvalue="Images added", offvalue="Images removed")
cb_images.pack()

paragraph = tk.StringVar()
cb_paragraphs = Checkbutton(root, text="Paragraphs", variable=paragraph, onvalue="Paragrahs added", offvalue="Paragraphs removed")
cb_paragraphs.pack()


download_btn = Button(root, text="Download", command=url_find)
download_btn.pack()

root.mainloop()

