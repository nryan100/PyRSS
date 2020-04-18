import unittest.test
from bs4 import BeautifulSoup
import sys

sys.path.append('../')
from pyrss.model.FeedParser import FeedParser

class TestParser(unittest.TestCase):

    TEST_FEED = "TestFeed.xml"

    def test_sample_feed_file(self):
        index = 1
        titleExpected = "Title {}"
        linkExpected = "https://www.item{}.com"
        descExpected = "Description {}"
        dateExpected = "Date {}"
        
        sample_Articles = FeedParser.parseSource(self.TEST_FEED,True)

        # Test that items in TestFeed.xml match their expected results
        for sample in sample_Articles:

            self.assertEqual(sample["title"], titleExpected.format(index))
            self.assertEqual(sample["link"], linkExpected.format(index))
            self.assertEqual(sample["desc"], descExpected.format(index))
            self.assertEqual(sample["date"], dateExpected.format(index))
            
            index += 1

    
    def test_article_contents(self):
        sample_Articles = FeedParser.parseSource(self.TEST_FEED,True)
        self.assertEqual(sample_Articles[0], {'title': 'Title 1', 'link': 'https://www.item1.com', 'date': 'Date 1', 'desc': 'Description 1'})
        

    def test_empty_source(self):
        errored_Articles = FeedParser.parseSource("",False)
        self.assertNotEqual(errored_Articles, None)

        errored_Articles = FeedParser.parseSource("",True)
        self.assertNotEqual(errored_Articles, None)


    def test_feed_url_extraction(self):
        articles = FeedParser.parseSource("https://rss.nytimes.com/services/xml/rss/nyt/DiningandWine.xml",False)
        self.assertNotEqual(articles, None)

        self.assertNotEqual(articles[0]["title"], None)
        self.assertNotEqual(articles[0]["link"], None)
        self.assertNotEqual(articles[0]["desc"], None)
        self.assertNotEqual(articles[0]["date"], None)


    def test_makeSoup_functionality(self):
        fp = FeedParser()
        # Tests both branches and checks that method returns BeautifuSoup object
        self.assertIsInstance(fp.makeSoup(self.TEST_FEED,True), BeautifulSoup)
        self.assertIsInstance(fp.makeSoup("https://rss.nytimes.com/services/xml/rss/nyt/DiningandWine.xml",False), BeautifulSoup)
        

    def test_error_handeling(self):
        # Throw file not found exception
        broken_Articles = FeedParser.parseSource("NotAFeed.xml", True)
        self.assertEqual(broken_Articles[0]["title"], "File 'NotAFeed.xml' was not found. Check directory & file name.")
        # Throw invalid URL format exception
        broken_Articles = FeedParser.parseSource("not.a.website.com", False)
        self.assertEqual(broken_Articles[0]["title"], "Invalid URL format for 'not.a.website.com'. Check URL.")
        # Throw an unhandeled generic exception 
        broken_Articles = FeedParser.parseSource("*", True)
        self.assertEqual(broken_Articles[0]["title"], "Error in '*', Check source.")
        self.assertNotEqual(broken_Articles[0]["desc"], None)
        # Ensure empty list is not returned if exception is not thrown 
        broken_Articles = FeedParser.parseSource("https://www.google.com", False)
        self.assertEqual(broken_Articles[0]["title"], "Source 'https://www.google.com' was not found")