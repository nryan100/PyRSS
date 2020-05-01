import tkinter as tk
from tkinter import colorchooser
import webbrowser
import sys
import os
 
sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))
from pyrss.model.FeedParser import FeedParser


class RSS_Display():

    # Time delay between each feed
    FEED_DELAY = 15000
    # Cut text at x characters
    CUT_AT = 80 
    
    ALWAYS_ON_TOP = True
    
    def __init__(self, master = None):

        self.master = master
        self.draw()

        self.source = ""
        self.isFile = ""
        self.articleIndex = 0
        self.articles = []


    def draw(self):
        if self.master is not None: 
            self.master.title("PyRSS")
            self.master.resizable(0,0)
            self.master.attributes("-topmost",self.ALWAYS_ON_TOP)
            self.bg_color = 'white'
            self.fg_color = 'black'
            self.label = tk.Label(
            self.master, font=("Helvetica", 10), cursor="hand2")
            self.label.pack()


    def generateArticles(self, source, isFile):
        self.source = source
        self.isFile = isFile
        self.articles = FeedParser.parseSource(source,isFile)


    def iterateArticles(self):
        
        # Assume errored return if only one element in articles. Formatting avoided to show entirety of error message 
        if len(self.articles) == 1: 
            self.master.title(self.articles[self.articleIndex]['fname'])
            self.label.configure(
                text = self.articles[self.articleIndex]['title'], bg='red'
                )
            self.articleIndex = 0
            self.articles = FeedParser.parseSource(self.source, self.isFile)
            self.label.after(30000, self.iterateArticles)
        
        if self.articleIndex == len(self.articles):
            self.articleIndex = 0
            self.articles = FeedParser.parseSource(self.source, self.isFile)
            self.iterateArticles()

        elif len(self.articles) > 1: 
            self.master.title(self.articles[self.articleIndex]['fname'])
            self.label.bind(
                "<Button-1>", lambda event : webbrowser.open_new_tab(self.articles[self.articleIndex - 1]['link']
                ))
            self.label.configure(
                text = self.cutText(self.articles[self.articleIndex]['title'], self.CUT_AT
                ), bg=self.bg_color, fg=self.fg_color)
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
        app = RSS_Display(root)
        app.generateArticles(source,isFile)
        app.iterateArticles()
        root.mainloop()


    #def backGround_color(self):
    #    bg_color1 = tk.colorchooser.askcolor(title='Background color selector')
    #    self.bg_color = bg_color1[1]
    #    self.label.configure(
    #        text=self.cutText(self.articles[self.articleIndex]['title'], self.CUT_AT
    #                         ), bg=self.bg_color)


    #def font_color(self):
    #    fnt_color = tk.colorchooser.askcolor(title='Background color selector')
    #    self.fg_color = fnt_color[1]
    #    self.label.configure(
    #        text=self.cutText(self.articles[self.articleIndex]['title'], self.CUT_AT
    #                          ), fg=self.fg_color)

    #def cycle_delay(self):
    #        pass

    #def menu(self):
    #    menu_bar = tk.Menu(self.master)
    #    self.master.config(menu=menu_bar)

    #    file = tk.Menu(menu_bar)
    #    menu_bar.add_cascade(label= 'File', menu=file)
    #    file.add_command(label='Exit', command= self.master.quit)

    #    view = tk.Menu(menu_bar)
    #    menu_bar.add_cascade(label='view', menu=view)
    #    view.add_command(label= 'Background Color', command=self.backGround_color)
    #    view.add_command(label= 'Font Color', command=self.font_color)
    #    view.add_command(label = 'Cycle Delay', command=self.cycle_delay)


#RSS_Display.run("TestRSSFeed.xml",True)
