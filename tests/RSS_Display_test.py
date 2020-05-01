import unittest.test
from unittest.mock import call, patch, PropertyMock
import tkinter as tk

from pyrss.view.RSS_Display import RSS_Display

class RSS_Display_test(unittest.TestCase):

    def test_case(self):
        self.assertEqual(1,1)

    def test_cutText(self):
        testString = "How are you?"
        testStringLength = len(testString)
            # Testing an empty String
        result1 = RSS_Display.cutText("", testStringLength)
        self.assertEqual(len(result1), 0)
            # Testing String with length below the limit
        result2 = RSS_Display.cutText(testString, testStringLength + 1)
        self.assertEqual(len(result2), testStringLength)
            # Testing with string above the limit
        result3 = RSS_Display.cutText(testString, testStringLength -1)
        self.assertEqual(len(result3), testStringLength - 1 + 3)
            # Testing with string at limit
        result4 = RSS_Display.cutText(testString, testStringLength)
        self.assertEqual(len(result4), testStringLength)


    def test_iterateArticles(self):
        with patch("pyrss.view.RSS_Display") as display: 
            root = tk.Tk()
            app = RSS_Display(root)

        # Test branch 1: if errored articles are returned
            app.generateArticles("Errored article", True)
            app.iterateArticles()
            # Check if the length of articles is 1
            self.assertEqual(len(app.articles), 1)
            # Assert that label's current text is not none
            self.assertNotEqual(app.label.cget("text"), None)

        # Test branch 2: if index == length of articles (i.e. a full iteration)
            #i.e. app.generateArticles("valid article", None)
            #Note: assert label.cget("text") for link and title
        # Test branch 3: if index < length of articles (update title and URL)
            # Same structure as above


    def test_run(self):
        with patch("pyrss.view.RSS_Display") as display: 
            root = tk.Tk()
            app = RSS_Display(root)
            app.generateArticles("TestRSSFeed.xml", True)
            app.iterateArticles()
            display.assert_has_calls(display.mainloop())


    def test_generateArticles(self):
        rd = RSS_Display()
        rd.generateArticles("TestRSSFeed.xml", True)
        self.assertIsNotNone(rd.articles)
        self.assertEqual(rd.articles[0]["title"], "Title 1")

