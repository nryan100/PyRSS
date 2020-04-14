from bs4 import BeautifulSoup
import requests

class FeedParser():

    def __init__(self, feed_file = None):
        self.feed_file = feed_file
        self.articles = []

    """
        Make a request and parse with beautifulsoup
    """
    def makeSoup(self,url):
        r = requests.get(str(url))
        return BeautifulSoup(r.text,"xml")

    """
        Parses an xml page and extracts the following: 
        - Title
        - Link
        - Date
        - Description
    """
    def parse(self,url):
        try: 
            for item in self.makeSoup(url).find_all("item"):                
                article = {
                    "title" : item.find_all("title")[0].get_text(),
                    "link"  : item.find_all("link")[0].get_text(),
                    "date"  : item.find_all("pubDate")[0].get_text(),
                    "desc"  : item.find_all("description")[0].get_text()
                }
                self.articles.append(article)
        except: 
            # TODO: FIX THIS!
            pass
            
        if not self.articles:
            self.articles.append({
                    "title":"URL: {} was not found".format(url),"link":"","date":"","desc": ""
                })


    """
        Parses a specific URL 
    """
    @staticmethod 
    def parseURL(url):
        fp = FeedParser()
        fp.parse(url)
        return fp.articles


    """
        Parses all feeds defined in a text file 
    """
    @staticmethod
    def parseFeedFile(file):
        pass


