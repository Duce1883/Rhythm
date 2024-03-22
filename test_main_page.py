from .pages.main_page import MainPage

link = "https://demoqa.com/"


class TestMainPage:

    def test_can_open_checkox_by_click_on_menu(self, browser):
        # ARRANGE
        page = MainPage(browser, link)
        page.open()

        # ACT & ASSERT
        page.click_on_elements_card()
        page.should_be_opened_elements_menu_is_presented()

        page.click_on_checkbox_item_in_side_menu()
        page.should_be_checkbox_page_open()

        page.click_on_home_directory_expand_btn()
        page.should_be_downloads_dir_presented()

        page.click_on_downloads_directory_expand_btn()
        page.should_be_wordfile_item_presented()

        page.click_on_wordfile_checkbox()
        page.should_be_wordfile_checkbox_checked()
        page.should_be_text_success_for_word_file_presented()
