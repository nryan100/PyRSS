import tkinter as tk
import webbrowser
import sys
import os
 
sys.path.append('../')
from model.FeedParser import FeedParser


class RSS_Display():

    # Time delay between each feed
    FEED_DELAY = 15000
    # Cut text at x characters
    CUT_AT = 80 
    
    ALWAYS_ON_TOP = True
    
    def __init__(self, master, source, isFile):
        self.master = master
        self.master.title("PyRSS")
        self.master.resizable(0,0)
        self.master.attributes("-topmost",self.ALWAYS_ON_TOP)

        self.source = source
        self.isFile = isFile
        self.articleIndex = 0

        self.label = tk.Label(
            master, font=("Helvetica", 10), cursor="hand2"
            )
        self.label.pack()
        # Fetch feeds before iterating
        self.articles = FeedParser.parseSource(source,isFile)
        # Begin loop
        self.iterateArticles()


    def iterateArticles(self):
        # Assume errored return if only one element in articles. Formatting avoided to show entirety of error message 
        if len(self.articles) == 1: 
            self.label.configure(
                text = self.articles[self.articleIndex]['title']
                )
            self.articleIndex = 0
            self.articles = FeedParser.parseSource(self.source, self.isFile)
            self.label.after(30000, self.iterateArticles)
        
        if self.articleIndex == len(self.articles):
            self.articleIndex = 0
            self.articles = FeedParser.parseSource(self.source, self.isFile)
            self.iterateArticles()

        elif len(self.articles) > 1: 
            self.label.bind(
                "<Button-1>", lambda event : webbrowser.open_new_tab(self.articles[self.articleIndex - 1]['link']
                ))
            self.label.configure(
                text = self.cutText(self.articles[self.articleIndex]['title'], self.CUT_AT
                ))
            self.articleIndex += 1
            self.label.after(self.FEED_DELAY, self.iterateArticles)

    
    @staticmethod
    def cutText(text,limit):
        if len(text) > limit: 
            return text[:limit] + "..."
        else: 
            return text


    @staticmethod    
    def run(source,isFile):
        root = tk.Tk()
        app = RSS_Display(root,source,isFile)
        root.mainloop()
    

RSS_Display.run("https://rss.nytimes.com/services/xml/rss/nyt/Music.xml", False)