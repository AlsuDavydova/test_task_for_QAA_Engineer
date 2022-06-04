from selenium.webdriver.common.by import By

class MainPageLocators():
    SEARCH_FIELD = (By.CSS_SELECTOR, "#text")
    SUGGEST_TABLE = (By.CSS_SELECTOR, "form[role=search]")
    SEARCH_RESULTS_TABLE = (By.CSS_SELECTOR, "ul#search-result")
    IMAGES_LINK = (By.CSS_SELECTOR, "[data-id=images]")

class ImagesPageLocators():
    FIRST_CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0 .PopularRequestList-SearchText")
    SEARCH_FIELD = (By.CSS_SELECTOR, "input.input__control")
    FIRST_IMAGE = (By.CSS_SELECTOR, "div.serp-item_pos_0 img.serp-item__thumb")
    OPENED_IMAGE = (By.CSS_SELECTOR,"img.MMImage-Origin")
    NEXT_BUTTON = (By.CSS_SELECTOR,".CircleButton_type_next")
    PREVIOUS_BUTTON =(By.CSS_SELECTOR,".CircleButton_type_prev")

     

    
