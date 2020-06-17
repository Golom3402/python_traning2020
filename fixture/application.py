# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(40)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")




    def return_to_groups_page(self):
        wd = self.wd
        # return to groups
        # wd.find_element_by_link_text("groups").click()
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd
        # init group creation
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # supbit
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def add_new_contact(self, contact):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_text_field_by_name('firstname', contact.first_name)
        self.fill_text_field_by_name('middlename', contact.middle_name)
        self.fill_text_field_by_name('lastname', contact.last_name)
        self.fill_text_field_by_name('nickname', contact.nickname)
        # self.fill_text_field_by_name(wd, 'photo', contact.photo)
        self.fill_text_field_by_name('title', contact.title)
        self.fill_text_field_by_name('company', contact.company)
        self.fill_text_field_by_name('address', contact.address)
        self.fill_text_field_by_name('home', contact.home_tel)
        self.fill_text_field_by_name('mobile', contact.mobile_tel)
        self.fill_text_field_by_name('work', contact.work_tel)
        self.fill_text_field_by_name('fax', contact.fax)
        self.fill_text_field_by_name('email', contact.email)
        self.fill_text_field_by_name('email2', contact.email2)
        self.fill_text_field_by_name('email3', contact.email3)
        self.fill_text_field_by_name('homepage', contact.homepage)
        self.choose_text_in_drop_down_list_by_name('bday', contact.b_day)
        self.choose_text_in_drop_down_list_by_name('bmonth', contact.b_month)
        self.fill_text_field_by_name('byear', contact.b_year)
        self.choose_text_in_drop_down_list_by_name('aday', contact.anny_day)
        self.choose_text_in_drop_down_list_by_name('amonth', contact.anny_month)
        self.fill_text_field_by_name('ayear', contact.anny_year)
        if contact.group:
            self.choose_text_in_drop_down_list_by_name('new_group', contact.group)
        self.fill_text_field_by_name('address2', contact.address2)
        self.fill_text_field_by_name('phone2', contact.phone2)
        self.fill_text_field_by_name('notes', contact.notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_text_field_by_name(self, text_field, text):
        wd = self.wd
        wd.find_element_by_name(text_field).click()
        wd.find_element_by_name(text_field).clear()
        wd.find_element_by_name(text_field).send_keys(text)

    def choose_text_in_drop_down_list_by_name(self, field_name, text):
        wd = self.wd
        wd.find_element_by_name(field_name).click()
        Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
        wd.find_element_by_name(field_name).click()

    def destroy(self):
        self.wd.quit()
