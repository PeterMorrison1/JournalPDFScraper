from selenium.webdriver.common.keys import Keys
from Scrapers.BaseSoup import BaseSoup


class BMJSoupScraper(BaseSoup):
    
    def __init__(self, url):
        super().__init__(url)

    def __get_article_button_element__(self):
        """Finds the element on the page for the button to click to get the pdf

        Returns:
            element: None if no element found / timeout or return driver element
        """
        element = super().__find_element_by_class__("article-pdf-download")
        return element
    
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
            return super().__get_pdf_url__(element, url, '/')
        else:
            return None
    