# -*- coding: utf-8 -*-
from selenium import webdriver
from lxml import etree, html
import cssselect
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd

        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name('MainForm')) > 0):
            wd.get(self.base_url)

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()

    def wait_element(self, locator):
        """
        метод ожидает появления на странице элемента
        :param locator: - кортеж. формат (By.XPATH, 'xpath')
        :return:
        """
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        element = wait.until(EC.visibility_of_element_located(locator))

