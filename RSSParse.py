import feedparser
import tkinter
from Article import Article
import time

#class Application(tkinter.Tk()):

    #def __init__(self,master):
    #    self.master = master

    #def draw(self,title):
    #    msg = tkinter.Message(self.master,text = title)
    #    msg.pack()

def getFeed():
    return feedparser.parse("https://www.cnbc.com/id/19854910/device/rss/rss.html")

def getData():
    articles = []

    for info in getFeed().entries:
        articles.append(Article(info['title'],info['link'],info['description']))

    return articles


for i in range(10):
    
    for data in getData():
        time.sleep(3)
        print(data.desc)

    time.sleep(10)

