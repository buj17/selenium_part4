from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_success_product_add(self):
        self.should_be_success_message()
        self.should_be_success_message_with_product_name()
        self.should_be_basket_total_equal_product_price()

    def should_be_success_message(self):
        assert (
            self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
        ), 'Success message is not presented, but should be'

    def should_not_be_success_message(self):
        assert (
            self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
        ), 'Success message is presented, but should not be'

    def should_be_success_message_with_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert (
                product_name == message_product_name
        ), f'Product name in message \'{message_product_name}\' does not match actual product name \'{product_name}\''

    def should_be_basket_total_equal_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert (
                product_price == basket_total
        ), f'Basket total \'{basket_total}\' does not match product price \'{product_price}\''

    def should_disappear_of_success_message(self):
        assert (
            self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
        ), 'Success message did not disappear'
