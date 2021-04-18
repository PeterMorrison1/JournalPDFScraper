from unittest import TestCase
from pprint import pprint
from Scrapers.ElsevierScraper import ElsevierScraper
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Elsevier_pdf_Test(TestCase):
    
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        cls.selenium_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.scraper = ElsevierScraper(cls.selenium_driver)
        
    @classmethod
    def tearDownClass(cls):
        cls.selenium_driver.quit()

        
    def test_pdf_open_access_article_should_pass(self):
        scraper = self.scraper
        url = "https://www.gastrojournal.org/article/S0016-5085(18)34810-8/fulltext"
        
        expected = "https://www.gastrojournal.org/action/showPdf?pii=S0016-5085%2818%2934810-8"
        actual = scraper.find_pdf_url(url)
        
        self.assertTrue(actual == expected, "Article pdf url was not found. Actual: " + str(actual))
        
    def test_pdf_open_access_article_lancet_should_pass(self):
        scraper = self.scraper
        url = "https://www.thelancet.com/journals/langas/article/PIIS2468-1253(19)30333-4/fulltext"
        
        expected = "https://www.thelancet.com/action/showPdf?pii=S2468-1253%2819%2930333-4"
        actual = scraper.find_pdf_url(url)
        
        self.assertTrue(actual == expected, "Article pdf url was not found. Actual: " + str(actual))
        
    def test_pdf_closed_access_article_should_fail(self):
        scraper = self.scraper
        url = "https://www.gastrojournal.org/article/S0016-5085(18)35206-5/fulltext"
        
        expected = None
        actual = scraper.find_pdf_url(url)

        self.assertTrue(actual is None, "Article pdf url was found (either now free or wrong url found) actual: " + str(actual))
        
        
    def test_pdf_wrong_journal_should_fail(self):
        scraper = self.scraper
        url = "https://www.sciencedirect.com/science/article/pii/S0022460X20300754"
        
        expected = None
        actual = scraper.find_pdf_url(url)

        self.assertTrue(actual is None, "Article pdf url was found, actual: " + str(actual))
    
    
    def test_url_open_access_article_should_pass(self):
        scraper = self.scraper
        url = "https://www.gastrojournal.org/article/S0016-5085(18)34810-8/fulltext"
        
        expected = "https://www.gastrojournal.org/action/showPdf?pii=S0016-5085%2818%2934810-8"
        actual = scraper.find_journal_url(url)
        
        self.assertTrue(actual == url, "Article pdf url was not found. Actual: " + str(actual))
        
    def test_url_open_access_article_lancet_should_pass(self):
        scraper = self.scraper
        url = "https://www.thelancet.com/journals/langas/article/PIIS2468-1253(19)30333-4/fulltext"
        
        expected = "https://www.thelancet.com/action/showPdf?pii=S2468-1253%2819%2930333-4"
        actual = scraper.find_journal_url(url)
        
        self.assertTrue(actual == url, "Article pdf url was not found. Actual: " + str(actual))
        
    def test_url_closed_access_article_should_fail(self):
        scraper = self.scraper
        url = "https://www.gastrojournal.org/article/S0016-5085(18)35206-5/fulltext"
        
        expected = None
        actual = scraper.find_journal_url(url)

        self.assertTrue(actual is None, "Article pdf url was found (either now free or wrong url found) actual: " + str(actual))
        
        
    def test_url_wrong_journal_should_fail(self):
        scraper = self.scraper
        url = "https://www.sciencedirect.com/science/article/pii/S0022460X20300754"
        
        expected = None
        actual = scraper.find_journal_url(url)

        self.assertTrue(actual is None, "Article pdf url was found, actual: " + str(actual))
        