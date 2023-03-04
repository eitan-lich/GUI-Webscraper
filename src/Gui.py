import tkinter as tk
from tkinter import messagebox

class Gui:
    def __init__(self):
        self.url = None
        self.window = tk.Tk(className=" GUI Webscraper").geometry("700x200")

    def setup_window(self):
        website_url_label = tk.Label(self.window,
                                     text="Enter the URL of the website you wish to scrape",
                                     padx=10,
                                     pady=10,
                                     font=('Helvetica 15 bold', 18),
                                     bg='#99CCFF')
        website_url_label.pack()
        website_url = tk.Entry(self.window, width=50)
        website_url.pack()
        button = tk.Button(self.window, text="Download raw HTML",
                           padx=2,
                           pady=2,
                           font=('Helvetica 15 bold', 10),
                           bg='#FFF')
        button.pack()
        self.url = website_url.get()

    def run(self):
        self.window.mainLoop()

    def get_url(self):
        return self.url

    def wrong_url(self):
        messagebox.showwarning("Missing/Invalid URL", "Must enter a valid URL")

