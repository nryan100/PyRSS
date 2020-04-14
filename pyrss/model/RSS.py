import feedparser
import webbrowser
import time

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


