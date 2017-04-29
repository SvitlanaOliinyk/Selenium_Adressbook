from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of, element_to_be_clickable
from selenium.webdriver.common.by import By


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def is_present(self):
        self.open_group_page()
        return self.app.is_element_present(By.NAME, 'selected[]')

    def delete_by_number(self, number):
        wd = self.app.wd
        checkboxes = wd.find_elements_by_name('selected[]')
        check = checkboxes[number]
        check.click()
        # WebDriverWait(wd, 15).until(staleness_of(check))
        bc = wd.find_element_by_name('delete')
        bc.click()
        WebDriverWait(wd, 15).until(staleness_of(bc))


    def open_group_page(self):
        wd = self.app.wd
        # Open group page
        wait = WebDriverWait(wd, 15)
        el = wait.until(element_to_be_clickable((By.XPATH, '//*[@id="nav"]/ul/li[3]/a')))
        el.click()
        WebDriverWait(wd, 15).until(staleness_of(el))

    def create(self, group):
        wd = self.app.wd
        # Init group creation
        # wd.find_element_by_name("new").click()  !!! Кнопка не успевает стать кликбл, поэтому валиться. решение ниже
        button = wd.find_element_by_name("new")
        button.click()
        WebDriverWait(wd, 15).until(staleness_of(button))
        # Fill group form
        if group.name is not None:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
        if group.header is not None:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
        if group.footer is not None:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group form
        wd.find_element_by_name("submit").click()

    def return_to_group_page(self):
        wd = self.app.wd
        # Return to group page
        # wd.find_element_by_link_text("group page").click()  !!! Не успевает вернуться на станицу. Делаем задержку
        bb = wd.find_element_by_link_text("group page")
        bb.click()
        WebDriverWait(wd, 15).until(staleness_of(bb))
