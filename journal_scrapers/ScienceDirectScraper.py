from selenium.webdriver.common.keys import Keys
from journal_scrapers.Base import Base

class ScienceDirectScraper(Base):
    
    def __init__(self, driver):
        super().__init__(driver)

    def __get_article_button_element__(self):
        """Finds the element on the page for the button to click to get the pdf

        Returns:
            element: None if no element found / timeout or return driver element
        """
        elements = super().__find_elements_by_id__("pdfLink")
        if elements is not None and len(elements) == 0:
            return None
        else:
            element = super().__click_element_wait_for_new_element__(elements[0].get_attribute("id"), "a.link-button-primary:nth-child(1)")
            return element

    def __get_download_url__(self):
        url = self.selenium_driver.find
    
    def can_parse_url(self, url):
        """Determines if the url can be parsed by the specific scraper

        Args:
            url (string): the url to scraped

        Returns:
            element: None if no element found / timeout or return driver element
        """
        super().__launch_journal_page__(url)

        element = self.__get_article_button_element__()

        if element is not None:
            return element
        else:
            return None

    def find_pdf_url(self, url):
        """Will find the free PDF url and return it

        Args:
            url (string): the url to scrape

        Returns:
            String: None if the article is pay-walled or if the url is invalid or if the scraper is outdated, otherwise return pdf url
        """
        super().__launch_journal_page__(url)
        
        element = self.__get_article_button_element__()
        if element is not None:
            super().__click_element__(element)
            pdf_url = super().__get_href_value__("save-pdf-icon-button")
            return pdf_url
        else:
            return None
    
    def find_journal_url(self, url):
        """Will find the free journal url and return it. Otherwise returns None. This is different than the pdf as it does not send the PDF page, only check if it is free.

        Args:
            url (string): the url of the journal page

        Returns:
            String: None if the article is pay-walled or if the url is invalid or if the scraper is outdated, otherwise return pdf url
        """
        super().__launch_journal_page__(url)
        
        element = self.__get_article_button_element__()
        if element is not None:
            return self.selenium_driver.current_url
        else:
            return None