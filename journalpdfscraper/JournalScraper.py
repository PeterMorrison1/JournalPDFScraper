from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from journalpdfscraper.Base import Base
from journalpdfscraper.ElsevierScraper import ElsevierScraper
from journalpdfscraper.ScienceDirectScraper import ScienceDirectScraper
from journalpdfscraper.BMJSoupScraper import BMJSoupScraper
from journalpdfscraper.OxfordScraper import OxfordScraper
import os

class JournalScraper():

    def __init__(self):
        """Initiates the Journal Scraper
        
        The Journal will go to each journal page that is sent to it, or provided in a list. The
         webdriver is provided by the online chrome source for now via pip, it will later be an optional input.
        """
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-notifications")
        options.add_argument("disable-infobars")
        options.add_argument("disable-gpu")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--start-maximized")
        self.selenium_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, service_log_path=os.devnull)
        
    def __end__(self):
        """Shuts down the selenium driver, ending the browser instance.
        """
        self.selenium_driver.quit()
        
    def __get_scrapers__(self, url):
        return [ElsevierScraper(self.selenium_driver), ScienceDirectScraper(self.selenium_driver), OxfordScraper(self.selenium_driver), BMJSoupScraper(url)]
        # TODO: Try to dynamically get all rather than hard code scrapers: return [obj() for obj in Base.__subclasses__()]
    
    def __find_correct_scraper__(self, url):
        for scraper in self.__get_scrapers__(url):
            if scraper.can_parse_url(url) is not None:
                return scraper
        
        return None
    
    def clear_instance(self):
        while len(self.selenium_driver.window_handles) > 1:
            self.selenium_driver.switch_to.window(self.selenium_driver.window_handles[-1])
            self.selenium_driver.close()
        self.selenium_driver.switch_to.window(self.selenium_driver.window_handles[0])
    
    def scrape_article(self, url):
        """Finds the url of the pdf if it is open access and exists

        Args:
            url (string): The url for the article to be scraped

        Returns:
            string: url of the pdf
        """
        #! Does not currently work due to complications with journal page scraping. See method 'check_if_article_is_free'
        scraper = self.__find_correct_scraper__(url)
        if scraper is not None:
            pdf_url = scraper.find_pdf_url(url)
            if pdf_url is not None:
                return pdf_url
            else:
                return False
        else:
            return 'No Supported Scraper Found for: ' + url


    def check_if_article_is_free(self, url):
        """Finds the url of the pdf if it is open access and exists

        Args:
            url (string): The url for the article to be scraped

        Returns:
            string: url of the pdf
        """
        scraper = self.__find_correct_scraper__(url)
        if scraper is not None:
            pdf_url = scraper.find_journal_url(url)
            if pdf_url is not None:
                return pdf_url
            else:
                return False
        else:
            return False

