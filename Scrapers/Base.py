from abc import ABC, abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import time

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
        if self.selenium_driver.current_url is not url:
            self.selenium_driver.get(url)
    
    def __find_elements_by_id__(self, id_name):
        try:
            elements = WebDriverWait(self.selenium_driver, self.delay).until(EC.presence_of_all_elements_located((By.ID, id_name)))
            return elements
        except TimeoutException:
            return []

    def __find_elements_by_class__(self, class_name):
        try:
            elements = WebDriverWait(self.selenium_driver, self.delay).until(EC.presence_of_all_elements_located((By.CLASS_NAME, class_name)))
            return elements
        except TimeoutException:
            return []

    def __click_button_wait_until_clickable_id__(self, element_id_name):
        WebDriverWait(self.selenium_driver, self.delay).until(EC.element_to_be_clickable((By.ID, element_id_name))).click()

    def __click_button_wait_until_clickable_class__(self, element_class_name):
        WebDriverWait(self.selenium_driver, self.delay).until(EC.element_to_be_clickable((By.CLASS_NAME, element_class_name))).click()

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
            self.selenium_driver.close()
            self.selenium_driver.switch_to.window(self.selenium_driver.window_handles[-1])

        # Wait until url changes or until timeout (delay)
        WebDriverWait(self.selenium_driver, self.delay).until(EC.url_changes(current_url))
        new_url = self.selenium_driver.current_url
        if new_url != current_url:
            return new_url
        else:
            return None

    def __click_element_wait_for_new_element__(self, element_1_id_name, element_2_css_selector):
        """This will click the passed element_1 then wait for element_2 to appear, then return that element

        Args:
            element_1_id_name (string): first element being clicked as an element id
            element_2_css_selector (string): second element being clicked as a css selector

        Returns:
            string: If timeout then return None, otherwise return the pdf url
        """
        self.__click_button_wait_until_clickable_id__(element_1_id_name)

        # Wait until the new element appears
        new_element = WebDriverWait(self.selenium_driver, self.delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, element_2_css_selector))
        )
        if new_element is not None:
            return new_element
        else:
            return None
        
    def __get_href_value__(self, element_id):
        """This will search for the passed element (by id) and return the href attribute

        Args:
            element_id (string): The element id being searched as an element id

        Returns:
            string: If timeout then return None, otherwise return the pdf url
        """
        new_element = WebDriverWait(self.selenium_driver, self.delay).until(
            EC.presence_of_element_located((By.ID, element_id))
        )
        if new_element is not None:
            return new_element.get_attribute("href")
        else:
            return None