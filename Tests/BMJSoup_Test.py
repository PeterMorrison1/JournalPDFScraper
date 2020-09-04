from unittest import TestCase
from pprint import pprint
from Scrapers.BMJSoupScraper import BMJSoupScraper
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class BMJSoup_Test(TestCase):
    
    def test_open_access_article_should_pass(self):
        # scraper = self.scraper
        url = "https://gut.bmj.com/content/68/9/1537"
        scraper = BMJSoupScraper(url)
        
        expected = "https://gut.bmj.com/content/gutjnl/68/9/1537.full.pdf"
        actual = scraper.find_pdf_url(url)
        
        self.assertTrue(actual.split("?")[0] == expected, "Article pdf url was not found. Actual: " + str(actual))
        
    def test_closed_access_article_should_fail(self):
        # scraper = self.scraper
        url = "https://academic.oup.com/jat/article-abstract/doi/10.1093/jat/bkaa070/5856455?redirectedFrom=fulltext"
        scraper = BMJSoupScraper(url)
        
        expected = None
        actual = scraper.find_pdf_url(url)

        self.assertTrue(actual is None, "Article pdf url was found (either now free or wrong url found) actual: " + str(actual))
        
    def test_wrong_journal_should_fail(self):
        # scraper = self.scraper
        url = "https://www.gastrojournal.org/article/S0016-5085(18)35206-5/fulltext"
        scraper = BMJSoupScraper(url)
        
        expected = None
        actual = scraper.find_pdf_url(url)

        self.assertTrue(actual is None, "Article pdf url was found, actual: " + str(actual))