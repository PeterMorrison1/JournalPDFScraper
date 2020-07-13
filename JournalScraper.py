from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Scrapers.Base import Base
from Scrapers.ElsevierScraper import ElsevierScraper

class JournalScraper():

    def __init__(self):
        """Initiates the Journal Scraper
        
        The Journal will go to each journal page that is sent to it, or provided in a list. The
         webdriver is provided by the online chrome source for now via pip, it will later be an optional input.
        """
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.selenium_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
    def __end__(self):
        """Shuts down the selenium driver, ending the browser instance.
        """
        self.selenium_driver.quit()
        
    def __get_scrapers__(self):
        print(Base.__subclasses__())
        return [ElsevierScraper(self.selenium_driver)]
        # TODO: Try to dynamically get all rather than hard code scrapers: return [obj() for obj in Base.__subclasses__()]
    
    def __find_correct_scraper__(self, url):
        for scraper in self.__get_scrapers__():
            if scraper.can_parse_url(url) is not None:
                return scraper
        
        return None
    
    def scrape_article(self, url):
        """Finds the url of the pdf if it is open access and exists

        Args:
            url (string): The url for the article to be scraped

        Returns:
            string: url of the pdf
        """
        scraper = self.__find_correct_scraper__(url)
        if scraper is not None:
            pdf_url = scraper.find_pdf_url(url)
            if pdf_url is not None:
                return pdf_url
            else:
                return None
        else:
            return None