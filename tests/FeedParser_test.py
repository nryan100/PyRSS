import unittest.test
from pyrss.model.FeedParser import FeedParser

class TestParser(unittest.TestCase):


    def test_sample_feed_file(self):
        index = 1
        titleExpected = "Title {}"
        linkExpected = "https://www.item{}.com"
        descExpected = "Description {}"
        dateExpected = "Date {}"
        
        sample_Articles = FeedParser.parseSource("TestFeed.xml",True)

        # Test that items in TestFeed.xml match their expected results
        for sample in sample_Articles:

            assert sample["title"] == titleExpected.format(index)
            assert sample["link"] == linkExpected.format(index)
            assert sample["desc"] == descExpected.format(index)
            assert sample["date"] == dateExpected.format(index)
            
            index += 1

    def test_article_contents(self):
        sample_Articles = FeedParser.parseSource("TestFeed.xml",True)
        assert sample_Articles[0] ==  {'title': 'Title 1', 'link': 'https://www.item1.com', 'date': 'Date 1', 'desc': 'Description 1'}
        

    def test_empty_source(self):
        errored_Article = FeedParser.parseSource("",False)
        assert errored_Article is not None
        assert errored_Article[0] == {'date': '', 'desc': '', 'link': '', 'title': 'Source  was not found'}

        errored_Article = FeedParser.parseSource("",True)
        assert errored_Article is not None
        assert errored_Article[0] == {'date': '', 'desc': '', 'link': '', 'title': 'Source  was not found'}


    def test_feed_url_extraction(self):
        pass

    def test_makeSoup_logic(self):
        pass

    def test_parseSource(self):
        pass

    def test_readFeedFile(self):
        pass
