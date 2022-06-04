from .main_page import MainPage
from .locators import ImagesPageLocators
import time

class ImagesPage(MainPage):

    def page_link(self,browser):
        assert "https://yandex.ru/images/" in browser.current_url

    def first_category(self):
        first_category = self.browser.find_element(*ImagesPageLocators.FIRST_CATEGORY)
        first_category_name = first_category.text
        first_category.click()
        time.sleep(3)
        search_field = self.browser.find_element(*ImagesPageLocators.SEARCH_FIELD)
        search_field_text = search_field.get_attribute("value")
        assert first_category_name == search_field_text

    def first_image(self):
        first_image = self.browser.find_element(*ImagesPageLocators.FIRST_IMAGE)
        first_image.click()
        #assert self.is_element_present(*ImagesPageLocators.OPENED_IMAGE)
        #assert self.browser.find_element(*ImagesPageLocators.FIRST_IMAGE).get_attribute("style")
        self.browser.execute_script("return arguments[0].complete && typeof arguments[0].naturalWidth != \"undefined\" && arguments[0].naturalWidth > 0", first_image)

    def should_open_second_image(self):
        first_image_link = self.browser.find_element(*ImagesPageLocators.OPENED_IMAGE).get_attribute("src")
        next_button = self.browser.find_element(*ImagesPageLocators.NEXT_BUTTON)
        next_button.click()
        time.sleep(3)
        second_image_link = self.browser.find_element(*ImagesPageLocators.OPENED_IMAGE).get_attribute("src")
        assert first_image_link != second_image_link

    def should_open_first_image(self):
        second_image_link = self.browser.find_element(*ImagesPageLocators.OPENED_IMAGE).get_attribute("src")
        previous_button = self.browser.find_element(*ImagesPageLocators.PREVIOUS_BUTTON)
        previous_button.click()
        time.sleep(3)
        first_image_link = self.browser.find_element(*ImagesPageLocators.OPENED_IMAGE).get_attribute("src")
        assert first_image_link != second_image_link
