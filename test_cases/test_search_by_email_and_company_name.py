import pytest
import time
from page_objects.login_page import LoginPage
from page_objects.add_customer import AddCustomer
from page_objects.search_customer_page import SearchCustomer
from utility.read_properties import ReadConfig


class TestSearchCustomerByEmailAndCompanyName:
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    @pytest.mark.email_and_company_name
    def test_search_customer_using_email_and_company_name(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(3)

        # login
        self.login_page = LoginPage(self.driver)
        self.login_page.set_user_name(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login_button()
        time.sleep(3)

        # check customer page
        self.add_customer = AddCustomer(self.driver)
        self.add_customer.click_customer_menu()
        self.add_customer.click_customer_menu_item()
        time.sleep(3)

        # search customer
        self.search_customer = SearchCustomer(self.driver)
        self.search_customer.set_email("kiyjcycyhjc676008@gmail.com")
        self.search_customer.set_company_name("Indian Cricket Team")
        self.search_customer.search_button()
        time.sleep(3)

        status = self.search_customer.search_customer_by_email("kiyjcycyhjc676008@gmail.com")
        assert True == status

        status = self.search_customer.search_customer_by_company_name("Indian Cricket Team")
        assert True == status
        self.driver.close()
