from bs4 import BeautifulSoup
import requests

class FeedParser():

    def __init__(self, feed_file = None):
        self.feed_file = feed_file
        self.articles = []


    """
        Parses an xml page and extracts the following: 
        - Title
        - Link
        - Date
        - Description
    """
    def parse(self,url):
        if self.validate(url):
            try: 
                soup = BeautifulSoup(requests.get(str(url)).text, 'xml')

                for item in soup.find_all("item"):                
                    article = {
                        "title" : item.find_all("title")[0].get_text(),
                        "link"  : item.find_all("link")[0].get_text(),
                        "date"  : item.find_all("pubDate")[0].get_text(),
                        "desc"  : item.find_all("description")[0].get_text()
                    }
                    self.articles.append(article)
                    #TODO REMOVE THIS LATER
                    print(article.values())
                    
            except: 
                #TODO ERROR HANDELING
                pass
        #TODO return empty / partial dict if invalid or unable to be read


    """
        TODO: check for .xml in url
    """
    @staticmethod
    def validate(url):
        return True


    """
        
    """
    @staticmethod 
    def parseURL(url):
        fp = FeedParser()
        fp.parse(url)
        return fp.articles

for item in FeedParser.parseURL("https://rss.nytimes.com/services/xml/rss/nyt/Music.xml"):
    print(item.values())
