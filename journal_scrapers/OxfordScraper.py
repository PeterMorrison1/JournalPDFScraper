from selenium.webdriver.common.keys import Keys
from journal_scrapers.Base import Base


class OxfordScraper(Base):
    
    def __init__(self, driver):
        super().__init__(driver)

    def __get_article_button_element__(self):
        """Finds the element on the page for the button to click to get the pdf

        Returns:
            element: None if no element found / timeout or return driver element
        """
        elements = super().__find_elements_by_class__("article-pdfLink")
        if len(elements) == 0:
            return None
        else:
            return elements[0]
    
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
            return super().__click_element__(element)
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
            if super().__find_elements_by_class__("captcha") is not None:
                return 'captcha'
            else:
                return None