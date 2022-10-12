from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import time



class ProductPage(BasePage):
    def should_be_product_page(self):
        assert "Coders at Work" == self.get_book_name(),"Name should be coders at work"
        assert "£19.99" == self.get_price(), "Price is not 19.99"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_NAME), \
        "Success message is presented, but should not be"
    
    def get_book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def get_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text
    
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
