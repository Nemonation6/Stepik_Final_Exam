from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
        
    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT)