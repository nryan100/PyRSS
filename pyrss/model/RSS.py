import feedparser
import webbrowser
import time


# def __init__(self, url):
#     self.url = url


def callBack(url):
    webbrowser.open_new(url)


def parse_RSS(url):
    return feedparser.parse(url)


def title_extract(index):
    entry = feed.entries[index]
    return entry.title


def entry_number():
    return len(feed.entries)


def get_titles():
    entry_number = len(feed.entries)
    titles = ""
    for item in range(0, entry_number):
        titles += (title_extract(item) + "\n")
    return titles.split("\n")



feed = parse_RSS('http://rss.cnn.com/rss/cnn_topstories.rss')
title = get_titles()
i = 0
print(F'number of entry: {entry_number()}')
while True:
    changeTime = 2 # maybe a def to return this so we can call it from view class (unless
    time.strftime("%c")
    try:
        print (f'{i}  {title[i]}')
        i += 1
        time.sleep(.5)

        if (i == entry_number()):
                i = 0
    except:
        pass



