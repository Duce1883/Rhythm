from selenium.webdriver.common.by import By


class MainPageLocators:
    CHECK_BOX_PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Check Box')]")
    DOWNLOADS_DIRECTORY_EXPAND_BTN = (By.CSS_SELECTOR, "ol li:nth-child(3) .rct-collapse-btn")
    DOWNLOADS_DIRECTORY_TITLE = (By.XPATH, "//span[@class='rct-title' and contains(text(), 'Downloads')]")
    DOWNLOADS_WORD_FILE_CHECKBOX = (By.CSS_SELECTOR, "ol li:nth-child(3) .rct-node-leaf:first-child .rct-checkbox")
    DOWNLOADS_WORD_FILE_CHECKBOX_CHECKED = (
        By.CSS_SELECTOR, "ol li:nth-child(3) .rct-node-leaf:first-child .rct-checkbox .rct-icon-check")
    DOWNLOADS_WORD_FILE_TITLE = (By.XPATH, "//span[@class='rct-title' and contains(text(), 'Word File.doc')]")
    ELEMENTS_BUTTON = (By.XPATH, "//div[@class='card-body' and .//h5[text()='Elements']]")
    HOME_CONTENT = (By.CSS_SELECTOR, '.home-content')
    HOME_DIRECTORY_EXPAND_BTN = (By.CSS_SELECTOR, ".check-box-tree-wrapper .rct-node-parent .rct-collapse-btn")
    SIDE_MENU_ELEMENTS_OPEN = (By.CSS_SELECTOR, ".accordion>.element-group .element-list.collapse.show")
    SIDE_MENU_ITEM_CHECK_BOX = (By.XPATH, "//span[contains(text(), 'Check Box')]")
    SIDE_MENU_ITEM_TEXT_BOX = (By.XPATH, "//span[contains(text(), 'Text Box')]")
    TEXT_SUCCESS_WORD_FILE = (By.XPATH, "//span[@class='text-success' and contains(text(), 'wordFile')]")
