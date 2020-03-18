#https://stackoverflow.com/questions/23482748/how-to-create-a-hyperlink-with-a-label-in-tkinter\  cite this code
#https://www.tutorialspoint.com/python_text_processing/python_reading_rss_feed.htm  cite this code

from tkinter import *
import webbrowser
import feedparser

def callback(url):
    webbrowser.open_new(url)

NewsFeed = feedparser.parse("http://rss.cnn.com/rss/cnn_topstories.rss")

print('Number of RSS posts :', len(NewsFeed.entries))

entry = NewsFeed.entries[1]
print('Post Title :', entry.title)
root = Tk()
root.title("News Stories")
link1 = Label(root, text=entry.title, cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("http://rss.cnn.com/rss/cnn_topstories.rss"))

root.mainloop()