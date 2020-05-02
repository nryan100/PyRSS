import unittest.test
from unittest.mock import call, patch, PropertyMock
import tkinter as tk

from pyrss.view.RSS_Display import RSS_Display

class RSS_Display_test(unittest.TestCase):

    def test_cutText(self):
        """ Tests RSS_Display.cutText() functionality and return values """
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
        """ Tests RSS_Display.iterateArticles() functionality """
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
        """ Tests RSS_Display instantiation using mocking """
        with patch("pyrss.view.RSS_Display") as display: 
            root = tk.Tk()
            app = RSS_Display(root)
            app.generateArticles("TestRSSFeed.xml", True)
            app.iterateArticles()
            display.assert_has_calls(display.mainloop())


    def test_generateArticles(self):
        """ Tests RSS_Display.generateArticles() testing return values and functionality """
        rd = RSS_Display()
        rd.generateArticles("TestRSSFeed.xml", True)
        self.assertIsNotNone(rd.articles)
        self.assertEqual(rd.articles[0]["title"], "Title 1")
        
        
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        hello_team = tk.Button(self)
        hello_team["text"] = "Hello Team 4\n(click me)"
        hello_team["command"] = self.say_hi
        hello_team.pack(side="top")

        quit = tk.Button(self, text="QUIT", fg="green", \
                              command=self.master.destroy)
        quit.pack(side="bottom")

    def say_hi(self):
        print("Hi Team 4!")


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


