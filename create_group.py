# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class CreateGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(10)
    
    def test_(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_group_page(wd)
        self.create_group(wd)
        self.return_to_group_page(wd)
        self.logout(wd)

    def open_home_page(self, wd):
        # Open homepage
        wd.get("http://localhost:8888/addressbook/")

    def login(self, wd):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")

    def open_group_page(self, wd):
        # Open group page
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def create_group(self, wd):
        # Init group creation
        wd.find_element_by_xpath(r'//*[@id="nav"]/ul/li[3]/a').click()
        # Fill group form
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("Client")
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("Client")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("SuperHead")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("Супер")
        # Submit group form
        wd.find_element_by_name("submit").click()

    def return_to_group_page(self, wd):
        # Return to group page
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        # Logout
        wd.find_element_by_css_selector('form[name="logout"] > a').click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
