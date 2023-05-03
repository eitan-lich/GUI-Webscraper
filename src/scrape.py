import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
import requests
import os
from bs4 import BeautifulSoup


def create(html, name, element=None):
    cwd = os.getcwd()
    folder = os.path.join(cwd, name)
    print(folder)
    if not os.path.exists(folder):
        os.mkdir(folder)

    if element is None:
        with open(f"{folder}/{name}.txt", "w", encoding="utf-8") as txt_file:
            txt_file.write(html)
    else:
        with open(f"{folder}/{name + ' ' + element}.txt", "w", encoding="utf-8") as txt_file:
            for line in html:
                txt_file.write(str(line) + "\n")


def download():
    url = url_string.get()
    if url == "":
        messagebox.showwarning("Missing URL", "Must enter a valid URL")
        return

    try:
        response = requests.get(url)
        if response.status_code != 200:
            messagebox.showwarning("Not a valid URL", "Make sure the URL starts with HTTP/HTTPS")
            return
    except requests.exceptions.MissingSchema:
        messagebox.showwarning("Not a valid URL", "Make sure the URL starts with HTTP/HTTPS")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string

    if selected.get() == "Full HTML":
        create(soup.prettify(), title)

    elif selected.get() == "Anchor tags":
        links = [link for link in soup.find_all('a')]
        create(links, title, "Anchor tags")

    elif selected.get() == "Images":
        images = [img for img in soup.find_all('img')]
        create(images, title, "Images")

    elif selected.get() == "Paragraphs":
        paragraphs = [p for p in soup.find_all('p')]
        create(paragraphs, title, "Paragraphs")
    else:
        messagebox.showwarning("No option selected", "Must select one of the options")
        return


def create_gui():
    global url_string
    global selected

    root = tk.Tk()
    root.title("GUI Webscraper")
    root.geometry("500x250")

    website_url_label = Label(root, text="Website URL:")
    website_url_label.pack()

    url_string = tk.StringVar()
    website_url = Entry(root, textvariable=url_string, width=50)
    website_url.pack()

    selected = tk.StringVar()
    rb_full_html = Radiobutton(root, text="Full HTML", value="Full HTML", variable=selected)
    rb_full_html.pack()

    rb_a_tags = Radiobutton(root, text="Anchor tags", value="Anchor tags", variable=selected)
    rb_a_tags.pack()

    rb_images = Radiobutton(root, text="Images", value="Images", variable=selected)
    rb_images.pack()

    rb_paragraphs = Radiobutton(root, text="Paragraphs", value="Paragraphs", variable=selected)
    rb_paragraphs.pack()

    download_btn = Button(root, text="Download", command=download)
    download_btn.pack()

    root.mainloop()
