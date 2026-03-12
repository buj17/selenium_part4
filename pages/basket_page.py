from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_be_products_in_basket()
        self.should_be_empty_basket_message()

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket contains products, but should be empty"

    def should_be_empty_basket_message(self):
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Your basket is empty" in empty_message, \
            f"Expected 'Your basket is empty' message, got: '{empty_message}'"
