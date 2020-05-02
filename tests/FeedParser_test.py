import os

import unittest.test
from bs4 import BeautifulSoup
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))
from pyrss.model.FeedParser import FeedParser


class TestParser(unittest.TestCase):


    def test_sample_rss_feed(self):
        """ Tests FeedParser.parse() functionality """
        index = 1
        feedTitleExpected = "Sample"
        titleExpected = "Title {}"
        linkExpected = "https://www.item{}.com"
        descExpected = "Description {}"
        dateExpected = "Date {}"
        
        for item in FeedParser.parseSource("TestRSSFeed.xml",True):
            self.assertEqual(item["title"], titleExpected.format(index))
            self.assertEqual(item["link"], linkExpected.format(index))
            self.assertEqual(item["desc"], descExpected.format(index))
            self.assertEqual(item["date"], dateExpected.format(index))
            self.assertEqual(item["fname"], feedTitleExpected)

            index += 1

    
    def test_sample_atom_feed(self):
        """ Tests atom feed handling """
        index = 1
        feedTitleExpected = "Sample"
        titleExpected = "Title {}"
        linkExpected = "https://www.item{}.com"
        descExpected = "Description {}"
        dateExpected = "Date {}"
        
        for item in FeedParser.parseSource("TestAtomFeed.xml",True):
            self.assertEqual(item["title"], titleExpected.format(index))
            self.assertEqual(item["link"], linkExpected.format(index))
            self.assertEqual(item["desc"], descExpected.format(index))
            self.assertEqual(item["date"], dateExpected.format(index))
            self.assertEqual(item["fname"], feedTitleExpected)

            index += 1
    

    def test_incomplete_feed(self):
        """ Tests error handling """
        self.assertEqual(FeedParser.parseSource("TestBrokenFeed.xml", True)[0]['desc'], "No description found")
        
    def test_empty_source(self):
        """ Tests error handling """
        errored_Articles = FeedParser.parseSource("",False)
        self.assertNotEqual(errored_Articles, None)

        errored_Articles = FeedParser.parseSource("",True)
        self.assertNotEqual(errored_Articles, None)


    def test_feed_url_extraction(self):
        """ Tests RSS feed URL dictionary entries """
        articles = FeedParser.parseSource("https://rss.nytimes.com/services/xml/rss/nyt/DiningandWine.xml",False)
        self.assertNotEqual(articles, None)

        self.assertNotEqual(articles[0]["title"], None)
        self.assertNotEqual(articles[0]["link"], None)
        self.assertNotEqual(articles[0]["desc"], None)
        self.assertNotEqual(articles[0]["date"], None)


    def test_makeSoup_functionality(self):
        """ Tests both branches in FeedParser.makeSoup """
        fp = FeedParser()
        # Tests both branches and checks that method returns BeautifuSoup object
        self.assertIsInstance(fp.makeSoup("TestBrokenFeed.xml",True), BeautifulSoup)
        self.assertIsInstance(fp.makeSoup("https://rss.nytimes.com/services/xml/rss/nyt/DiningandWine.xml",False), BeautifulSoup)
        

    def test_error_handling(self):
        """ Tests all exception branches """
        # Throw file not found exception
        broken_Articles = FeedParser.parseSource("NotAFeed.xml", True)
        self.assertEqual(broken_Articles[0]["title"], "File 'NotAFeed.xml' was not found. Check directory & file name.")
        # Throw invalid URL format exception
        broken_Articles = FeedParser.parseSource("not.a.website.com", False)
        self.assertEqual(broken_Articles[0]["title"], "Invalid URL format for 'not.a.website.com'. Check URL.")
        # Ensure empty list is not returned if exception is not thrown 
        broken_Articles = FeedParser.parseSource("https://www.google.com", False)
        self.assertEqual(broken_Articles[0]["title"], "Source 'https://www.google.com' was not found")