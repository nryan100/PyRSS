from bs4 import BeautifulSoup
import requests

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
    def parse(self,source, isFile):
        try: 
            for item in self.makeSoup(source,isFile).find_all("item"):                
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
                    "title":"Source {} was not found".format(source),"link":"","date":"","desc": ""
                })


    """
        Parses a specific URL 
    """
    @staticmethod 
    def parseSource(source,isFile):
        fp = FeedParser()
        fp.parse(source,isFile)
        return fp.articles


    """
        Parses all feeds defined in a text file 
    """
    @staticmethod
    def parseFeedFile(file):
        pass