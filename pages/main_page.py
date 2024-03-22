from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def click_on_checkbox_item_in_side_menu(self):
        elem = self.browser.find_element(*MainPageLocators.SIDE_MENU_ITEM_CHECK_BOX)
        elem.click()

    def click_on_downloads_directory_expand_btn(self):
        elem = self.browser.find_element(*MainPageLocators.DOWNLOADS_DIRECTORY_EXPAND_BTN)
        elem.click()

    def click_on_elements_card(self):
        elem = self.browser.find_element(*MainPageLocators.ELEMENTS_BUTTON)
        elem.click()

    def click_on_home_directory_expand_btn(self):
        elem = self.browser.find_element(*MainPageLocators.HOME_DIRECTORY_EXPAND_BTN)
        elem.click()

    def click_on_wordfile_checkbox(self):
        elem = self.browser.find_element(*MainPageLocators.DOWNLOADS_WORD_FILE_CHECKBOX)
        elem.click()

    def should_be_home_page_content(self):
        assert self.is_element_present(
            *MainPageLocators.HOME_CONTENT), "Home page content is not presented"

    def should_be_checkbox_page_open(self):
        assert self.is_element_present(
            *MainPageLocators.CHECK_BOX_PAGE_TITLE), "Title of Checkbox page is not presented"

    def should_be_downloads_dir_presented(self):
        assert self.is_element_present(
            *MainPageLocators.DOWNLOADS_DIRECTORY_TITLE), "Directory 'Downloads' is not presented"

    def should_be_opened_elements_menu_is_presented(self):
        assert self.is_element_present(
            *MainPageLocators.SIDE_MENU_ELEMENTS_OPEN), "Opened 'Elements' menu is not presented"

    def should_be_text_success_for_word_file_presented(self):
        assert self.is_element_present(
            *MainPageLocators.TEXT_SUCCESS_WORD_FILE), "Text 'wordFile' is not presented in result"

    def should_be_wordfile_checkbox_checked(self):
        assert self.is_element_present(
            *MainPageLocators.DOWNLOADS_WORD_FILE_CHECKBOX_CHECKED), "Checked 'Word File' checkbox is not presented"

    def should_be_wordfile_item_presented(self):
        assert self.is_element_present(
            *MainPageLocators.DOWNLOADS_WORD_FILE_TITLE), "'Word File' is not presented"
