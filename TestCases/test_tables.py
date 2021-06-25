from selenium import webdriver
from page_objects.main_page import MainPageObjects
from page_objects.table_pagination_objects import TablePagination
from page_objects.table_data_search_objects import TableDataSearch
from TestData.statuses import Statuses
import pytest


@pytest.mark.usefixtures("setup")
class TestTable:

    @pytest.fixture(params=Statuses.getstatus)
    def status(self, request):
        return request.param

    @pytest.mark.skip
    def test_table_pagination(self):
        main_page_obj = MainPageObjects(self.driver)
        pagination_obj = TablePagination(self.driver)
        main_page_obj.expand_table()
        main_page_obj.click_table_pagination()
        pagination_obj.verify_table_pagination()

    def test_table_data_search(self, status):
        main_page_obj = MainPageObjects(self.driver)
        search_obj = TableDataSearch(self.driver)
        main_page_obj.expand_table()
        main_page_obj.click_table_data_search()
        search_obj.search_by(status.get("status"))
