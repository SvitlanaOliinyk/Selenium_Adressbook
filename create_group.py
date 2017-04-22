# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from model.group import Group


class CreateGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(10)
    
    def test_group(self):
        test_data_group = Group(name='Client', header='SuperHead', footer='Супер')
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_group_page()
        self.create_group(test_data_group)
        self.return_to_group_page()
        self.logout()

    def open_home_page(self):
        # Open homepage
        wd = self.wd
        wd.get("http://localhost:8888/addressbook/")

    def login(self, username, password):
        # login
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)

    def open_group_page(self):
        # Open group page
        wd = self.wd
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def create_group(self, group):
        # Init group creation
        wd = self.wd
        wd.find_element_by_xpath(r'//*[@id="nav"]/ul/li[3]/a').click()
        # Fill group form
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group form
        wd.find_element_by_name("submit").click()

    def return_to_group_page(self):
        # Return to group page
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        # Logout
        wd = self.wd
        wd.find_element_by_css_selector('form[name="logout"] > a').click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
