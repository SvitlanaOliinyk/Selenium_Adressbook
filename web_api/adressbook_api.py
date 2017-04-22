from selenium import webdriver

class AdressbookAPI:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)

    def open_home_page(self):
        wd = self.wd
        # Open homepage
        wd.get("http://localhost:8888/addressbook/")

    def login(self, username, password):
        wd = self.wd
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)

    def open_group_page(self):
        wd = self.wd
        # Open group page
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def create_group(self, group):
        wd = self.wd
        # Init group creation
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
        wd = self.wd
        # Return to group page
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        # Logout
        self.wd.find_element_by_css_selector('form[name="logout"] > a').click()

    def destroy(self):
        self.wd.quit()