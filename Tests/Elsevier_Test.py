from unittest import TestCase
from pprint import pprint
from JournalScraper import JournalScraper

class Elsevier_Test(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.scraper = JournalScraper()
        
    @classmethod
    def tearDownClass(cls):
        cls.scraper.__end__()
        
    def test_open_access_article_should_pass(self):
        scraper = self.scraper
        url = "https://www.gastrojournal.org/article/S0016-5085(18)34810-8/fulltext"
        
        expected = "https://www.gastrojournal.org/action/showPdf?pii=S0016-5085%2818%2934810-8"
        actual = scraper.scrape_article(url)
        
        print(actual)
        
        self.assertTrue(actual == expected, "Article pdf url was not found. Actual: " + str(actual))
        
    def test_closed_access_article_should_fail(self):
        scraper = self.scraper
        url = "https://www.gastrojournal.org/article/S0016-5085(18)35206-5/fulltext"
        
        expected = None
        actual = scraper.scrape_article(url)
        print(actual)

        self.assertTrue(actual is None, "Article pdf url was found (either now free or wrong url found) actual: " + str(actual))
        