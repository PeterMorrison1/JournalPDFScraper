from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class JournalScraper():

    def __init__(self):
        """Initiates the Journal Scraper
        
        The Journal will go to each journal page that is sent to it, or provided in a list. The
         webdriver is provided by the online chrome source for now via pip, it will later be an optional input.
        """
        
        