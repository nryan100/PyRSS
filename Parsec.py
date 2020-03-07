import feedparser as fp
from bs4 import BeautifulSoup
from pathlib import Path
import os
import tkinter as tk
import threading
import itertools
import webbrowser

'''
https://stackoverflow.com/questions/2697039/python-equivalent-of-setinterval
'''
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def getFeedURLs(filename):
    f = open(filename)
    soup = BeautifulSoup(f.read(), 'xml')
    feeds = []
    for url in soup.find_all('url'):
        feeds.append(url.contents[0])
    return feeds

def get_label_functor(label, app):

    def update():
        url = app.urls[app.count]
        parsed_feed = fp.parse(url)
        if parsed_feed["feed"]:
            if not app.mapToEntries[url]:
                app.mapToEntries[url] = itertools.cycle(parsed_feed["entries"])
            rss_entry = next(app.mapToEntries[url])
            label.set(rss_entry.title)
            app.current_url = rss_entry.link
        app.count = (app.count + 1) % len(app.urls)
    return update

class Application(tk.Frame):
    def __init__(self, urls,  master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.urls = urls
        self.current_url = None
        self.count = 0;
        self.mapToEntries = dict([(key, None) for key in self.urls])
        self.create_widgets()

    def create_widgets(self):
        stv = tk.StringVar()
        stv.set("loading feed...")
        lbl = tk.Label(self.master, textvariable=stv, fg="blue", cursor="hand2")
        lbl.bind("<Button-1>", lambda event: webbrowser.open_new_tab(app.current_url))
        set_interval(get_label_functor(stv, self), 2)
        lbl.pack()

if __name__ == "__main__":
    fn = str(Path.home()) + "/.jrsst"
    if os.path.exists(fn):
        urls = getFeedURLs(fn);
        root = tk.Tk()
        root.geometry("500x100+300+300")
        root.title("RSS Feeds")
        app = Application(urls, master=root)
        app.mainloop()




