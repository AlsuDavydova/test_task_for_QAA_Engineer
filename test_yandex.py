import pytest
from selenium import webdriver
from .main_page import MainPage
from .images_page import ImagesPage

class TestMainPage():

    def test_yandex_should_find_tensor_site(self, browser):
        link = "https://yandex.ru/"
        page = MainPage(browser, link)   
        page.open()                    
        page.yandex_search()

    def test_yandex_images_should_work_correctly(self, browser):
        link = "https://yandex.ru/"
        page = MainPage(browser, link)   
        page.open()
        page.should_be_yandex_images_link()
        page = browser.window_handles[1]
        browser.switch_to.window(page)
        page = ImagesPage(browser, link)   
        page.page_link(browser)
        page.first_category()
        page.first_image()
        page.should_open_second_image()
        page.should_open_first_image()
        
        
