from bs4 import BeautifulSoup
import requests
import sys
import time

class FeedParser():


    def __init__(self, feed_file = None):
        self.feed_file = feed_file
        self.articles = []


    """
        Make a request and parse with beautifulsoup
    """
    def makeSoup(self, source, isFile):
        if isFile: 
            with open(source, encoding="utf-8") as file:
                content = file.read()
            return BeautifulSoup(content,"xml")
        else:     
            r = requests.get(str(source))
            return BeautifulSoup(r.text,"xml")


    """
        Parses an xml page and extracts the following: 
        - Title
        - Link
        - Date
        - Description
    """
    def parse(self, source, isFile):

        try: 
            soup = self.makeSoup(source,isFile)            
            # assumes feeds with <item> tag belong to a RSS feed
            if len(soup.find_all("item")) > 0:
                feedName = soup.find("title").get_text()
                for item in soup.find_all("item"):
                    self.appendArticle(
                        item, "title", "link", "pubDate", "description", feedName, time.asctime( time.localtime(time.time()))
                    )
                    
            # assumes feeds with <entry> tag belong to an ATOM feed
            elif len(soup.find_all("entry")) > 0:
                feedName = soup.find("title").get_text()
                for item in soup.find_all("entry"):
                    self.appendArticle(
                        item, "title", "link", "updated", "summary", feedName, time.asctime( time.localtime(time.time()))
                    )

        except requests.exceptions.MissingSchema:
            self.articles.append({
                    "title": "Invalid URL format for '{}'. Check URL.".format(source),"link":"","date":"","desc": "", "fname" : "Error", "ftime" : ""
                })
        
        except FileNotFoundError:
            self.articles.append({
                    "title": "File '{}' was not found. Check directory & file name.".format(source),"link":"","date":"","desc": "", "fname" : "Error", "ftime" : ""
                })
        
        except Exception as e: 
            self.articles.append({
                    "title": "Source '{}' was not found. Check configuration".format(source),"link":"","date":"","desc": e, "fname" : "Error", "ftime" : ""
                })
            
        if not self.articles:
            self.articles.append({
                    "title":"Source '{}' was not found".format(source),"link":"","date":"","desc": "", "fname" : "Error", "ftime" : ""
                })


    """
        Dictionary interface. Uses tag names for search parameters and appends entry to articles array 
    """
    def appendArticle(self, item, titleTag, linkTag, dateTag, descTag, feedName, fetchTime): 
        try:
            article = {
                "title" : item.find(titleTag).get_text(),
                "link"  : item.find(linkTag).get_text(),
                "date"  : item.find(dateTag).get_text(),
                "desc"  : item.find(descTag).get_text(),
                "fname" : feedName, 
                "ftime" : fetchTime
            }
            self.articles.append(article)
        # If description is not found: 
        except Exception as error: 
            if item.find(titleTag) is not None and item.find(linkTag) is not None and item.find(dateTag) is not None: 
                article = {
                    "title" : item.find(titleTag).get_text(),
                    "link"  : item.find(linkTag).get_text(),
                    "date"  : item.find(dateTag).get_text(),
                    "desc"  : "No description found",
                    "fname" : feedName, 
                    "ftime" : fetchTime
                }
                self.articles.append(article)

    """
        Parses a specific URL 
    """
    @staticmethod 
    def parseSource(source,isFile):
        fp = FeedParser()
        fp.parse(source,isFile)
        return fp.articles

    @staticmethod
    def parseFeedFile(source):
        pass