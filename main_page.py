from .locators import MainPageLocators

class MainPage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
    def yandex_search(self):
        search_textarea = self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        search_textarea.send_keys("Тензор")
        search_suggestion = self.browser.find_element(*MainPageLocators.SUGGEST_TABLE)
        search_textarea.send_keys("\n")
        search_results = self.browser.find_element(*MainPageLocators.SEARCH_RESULTS_TABLE)
        tensor_link = self.browser.find_element_by_link_text("tensor.ru") 

    def should_be_yandex_images_link(self):
        images_link = self.browser.find_element(*MainPageLocators.IMAGES_LINK)
        images_link.click()
