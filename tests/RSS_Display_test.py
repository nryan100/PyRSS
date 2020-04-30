import unittest.test
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
        print(result3)
        self.assertEqual(len(result3), testStringLength - 1 + 3)
            # Testing with string at limit
        result4 = RSS_Display.cutText(testString, testStringLength)
        self.assertEqual(len(result4), testStringLength)