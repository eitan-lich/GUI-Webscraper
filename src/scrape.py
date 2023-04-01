import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
import requests
import os
from bs4 import BeautifulSoup


def create(html, name):
    cwd = os.getcwd()
    dir = os.path.join(cwd, "scrape files")
    if not os.path.exists(dir):
        os.mkdir(dir)

    os.chdir(dir)
    with open(f"{name}.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(html)


def create_from_list(html, name):
    cwd = os.getcwd()
    dir = os.path.join(cwd, "scrape files")
    if not os.path.exists(dir):
        os.mkdir(dir)

    os.chdir(dir)
    with open(f"{name}.txt", "w", encoding="utf-8") as txt_file:
        for line in html:
            print(str(line))
            txt_file.write(str(line)+"\n")


def download():
    url = url_string.get()
    if url == "":
        messagebox.showwarning("Missing/Invalid URL", "Must enter a valid URL")
        return

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string

    if selected.get() == "Full HTML":
        create(soup.prettify(), title)

    elif selected.get() == "Anchor tags":
        links = [link for link in soup.find_all('a')]
        create_from_list(links, title+" Anchor tags")

    elif selected.get() == "Images":
        images = [img for img in soup.find_all('img')]
        create_from_list(images, title+" Images")

    elif selected.get() == "Paragraphs":
        paragraphs = [p for p in soup.find_all('p')]
        create_from_list(paragraphs, title+" Paragraphs")

    else:
        messagebox.showwarning("No option selected", "Must select one of the options")
        return


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

