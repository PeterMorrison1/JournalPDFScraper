from abc import ABC, abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver

class Base(ABC):
    delay = 5
    
    def __init__(self, selenium_driver):
        self.selenium_driver = selenium_driver
        
    @abstractmethod
    def find_pdf_url(self, url):
        pass
    
    @abstractmethod
    def can_parse_url(self, url):
        pass

    def __launch_journal_page__(self, url):
        self.selenium_driver.get(url)
        return None
        
    def __find_elements_by_id__(self, id_name):
        #TODO: Keeping this for possible efficiency improvement: return WebDriverWait(self.selenium_driver, self.delay)
        #   .until(EC.presence_of_all_elements_located(self.selenium_driver.find_elements_by_id(id_name)))
        try:
            elements = self.selenium_driver.find_elements_by_id_name(id_name)
            return elements
        except TimeoutException:
            return None

    def __find_elements_by_class__(self, class_name):
        try:
            elements = self.selenium_driver.find_elements_by_class_name(class_name)
            return elements
        except TimeoutException:
            return None

    def __click_element__(self, element):
        """This will click the passed element, and if doing so opens a new tab, it will open the tab and check the new url

        Args:
            element (element): The driver element being clicked (button)

        Returns:
            string: If timeout then return None, otherwise return the pdf url
        """
        current_url = self.selenium_driver.current_url
        element.click()

        # Checks if clicking the element opened a new tab, if so moves focus to this tab
        if len(self.selenium_driver.window_handles) > 1:
            self.selenium_driver.switch_to.window(self.selenium_driver.window_handles[1])

        # Wait until url changes or until timeout (delay)
        WebDriverWait(self.selenium_driver, self.delay).until(EC.url_changes(current_url))
        new_url = self.selenium_driver.current_url
        if new_url != current_url:
            return new_url
        else:
            return None