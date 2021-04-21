from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests


class BaseSoup(ABC):
    delay = 5
    
    def __init__(self, url):
        page = requests.get(url)

        self.soup = BeautifulSoup(page.content, 'html.parser')
        
    @abstractmethod
    def find_pdf_url(self, url):
        pass
    
    @abstractmethod
    def can_parse_url(self, url):
        pass

    def __launch_journal_page__(self, url):
        if self.soup.current_url is not url:
            page = requests.get(url)

            self.soup = BeautifulSoup(page.content, 'html.parser')
    
    def __find_element_by_id__(self, id_name):
        element = self.soup.find(id=id_name)
        return element
        
    def __find_element_by_class__(self, class_name):
        element = self.soup.find(class_=class_name)
        return element

    def __get_pdf_url__(self, element, url, rsplit):
        url_base = url.rsplit(rsplit, 1)[0]
        new_url = url_base + element.value
        return new_url