from unittest import TestCase
from pprint import pprint
from Scrapers.OxfordScraper import OxfordScraper
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Oxford_Test(TestCase):
    
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        cls.selenium_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.scraper = OxfordScraper(cls.selenium_driver)
        
    @classmethod
    def tearDownClass(cls):
        cls.selenium_driver.quit()

        
    def test_open_access_article_should_pass(self):
        scraper = self.scraper
        url = "https://academic.oup.com/jcag/article/2/Supplement_1/S73/5099120"
        
        expected = "https://watermark.silverchair.com/gwy053.pdf"
        actual = scraper.find_pdf_url(url)
        
        self.assertTrue(actual.split("?")[0] == expected, "Article pdf url was not found. Actual: " + str(actual))
        
    def test_closed_access_article_should_fail(self):
        scraper = self.scraper
        url = "https://academic.oup.com/jat/article-abstract/doi/10.1093/jat/bkaa070/5856455?redirectedFrom=fulltext"
        
        expected = None
        actual = scraper.find_pdf_url(url)

        self.assertTrue(actual is None, "Article pdf url was found (either now free or wrong url found) actual: " + str(actual))
        
    def test_wrong_journal_should_fail(self):
        scraper = self.scraper
        url = "https://www.gastrojournal.org/article/S0016-5085(18)35206-5/fulltext"
        
        expected = None
        actual = scraper.find_pdf_url(url)

        self.assertTrue(actual is None, "Article pdf url was found, actual: " + str(actual))