# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from contact_model import Contact
import unittest, time, re

class AddNewGontact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def test_add_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, name='admin', password='secret')
        contact = Contact(first_name='Test_user1', middle_name='Петрович', last_name="Ватутин", nickname="Test1",
                photo="C:\\fakepath\\Koala.jpg", title='TutleTest data1', company='E-corp', address='York sheer 13',
                home_tel='+3-9-99-99-9-9-9', work_tel='+7-495-399-59-59', mobile_tel='+79291929929', fax='3334528',
                email='petrovi4@mail.ru', email2='test1@yandex.ru', email3='vatutin123@gmail.com',
                homepage='www.facebook.com', b_day='14', b_month='December', b_year='1944', anny_day='14',
                anny_month='April', anny_year='1994', group=None, address2='address 2 2 2', phone2='123456789-0',
                notes='notes notes notes notes notes notes notes notes notes notes notes notes notes notes')
        self.open_home_page(wd)
        self.add_new_contact(wd, contact=contact)
        self.return_to_home_page(wd)

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def add_new_contact(self, wd, contact):
        wd.find_element_by_link_text("add new").click()
        self.fill_text_field_by_name(wd, 'firstname', contact.first_name)
        self.fill_text_field_by_name(wd, 'middlename', contact.middle_name)
        self.fill_text_field_by_name(wd, 'lastname', contact.last_name)
        self.fill_text_field_by_name(wd, 'nickname', contact.nickname)
        # self.fill_text_field_by_name(wd, 'photo', contact.photo)
        self.fill_text_field_by_name(wd, 'title', contact.title)
        self.fill_text_field_by_name(wd, 'company', contact.company)
        self.fill_text_field_by_name(wd, 'address', contact.address)
        self.fill_text_field_by_name(wd, 'home', contact.home_tel)
        self.fill_text_field_by_name(wd, 'mobile', contact.mobile_tel)
        self.fill_text_field_by_name(wd, 'work', contact.work_tel)
        self.fill_text_field_by_name(wd, 'fax', contact.fax)
        self.fill_text_field_by_name(wd, 'email', contact.email)
        self.fill_text_field_by_name(wd, 'email2', contact.email2)
        self.fill_text_field_by_name(wd, 'email3', contact.email3)
        self.fill_text_field_by_name(wd, 'homepage', contact.homepage)
        self.choose_text_in_drop_down_list_by_name(wd, 'bday', contact.b_day)
        self.choose_text_in_drop_down_list_by_name(wd, 'bmonth', contact.b_month)
        self.fill_text_field_by_name(wd, 'byear', contact.b_year)
        self.choose_text_in_drop_down_list_by_name(wd, 'aday', contact.anny_day)
        self.choose_text_in_drop_down_list_by_name(wd, 'amonth', contact.anny_month)
        self.fill_text_field_by_name(wd, 'ayear', contact.anny_year)
        if contact.group:
            self.choose_text_in_drop_down_list_by_name(wd, 'new_group', contact.group)
        self.fill_text_field_by_name(wd, 'address2', contact.address2)
        self.fill_text_field_by_name(wd, 'phone2', contact.phone2)
        self.fill_text_field_by_name(wd, 'notes', contact.notes)

        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_text_field_by_name(self, wd, text_field, text):
        wd.find_element_by_name(text_field).click()
        wd.find_element_by_name(text_field).clear()
        wd.find_element_by_name(text_field).send_keys(text)

    def choose_text_in_drop_down_list_by_name(self, wd, field_name, text):
        wd.find_element_by_name(field_name).click()
        Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
        wd.find_element_by_name(field_name).click()

    def login(self, wd, name, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
