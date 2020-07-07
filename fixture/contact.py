import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from model.contact_model import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def edit(self, old_contact, new_contact):
        wd = self.app.wd
        title = old_contact.first_name+' '+old_contact.last_name
        locator=f'// input[ @ type = "checkbox" and contains( @ title, "{title}")]/../following-sibling::td/a/img[@title="Edit"]'
        wd.find_element_by_xpath(locator).click()
        self.fill_contact_form(new_contact)
        wd.find_element_by_name('update').click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self, new_contact):
        self.edit_contact_by_index(0, new_contact)

    def edit_contact_by_index(self, index, new_contact):
        wd = self.app.wd
        self.app.open_home_page()
        locator = '//td/a/img[@title="Edit"]'
        edit_buttons = wd.find_elements_by_xpath(locator)
        edit_buttons[index].click()
        self.fill_contact_form(new_contact)
        wd.find_element_by_name('update').click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        locator = '//td/input[@type="checkbox"]'
        all_check_boxes = wd.find_elements_by_xpath(locator)
        all_check_boxes[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        alert = wd.switch_to_alert()
        alert.accept()
        self.contact_cache = None

    def delete(self, contact):
        wd = self.app.wd
        title = contact.first_name + ' ' + contact.last_name
        locator = f'// input[ @ type = "checkbox" and contains( @ title, "{title}")]'
        wd.find_element_by_xpath(locator).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        alert = wd.switch_to_alert()
        alert.accept()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_xpath("//table//tr//input"))




    def fill_contact_form(self, contact):
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

    def fill_text_field_by_name(self, text_field, text):
        wd = self.app.wd
        if text:
            wd.find_element_by_name(text_field).click()
            wd.find_element_by_name(text_field).clear()
            wd.find_element_by_name(text_field).send_keys(text)
        else:
            pass

    def choose_text_in_drop_down_list_by_name(self, field_name, text):
        wd = self.app.wd
        if text:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).click()
        else:
            pass

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.app.wait_element((By.XPATH, "//tbody/tr/th[3]/a"))
            self.contact_cache=[]
            self.app.wait_element((By.NAME, "entry"))
            for element in wd.find_elements_by_name("entry"):
                cont_id = element.find_element_by_xpath("./td/input").get_attribute('value')
                last_name = element.find_element_by_xpath("./td[2]").text
                first_name = element.find_element_by_xpath("./td[3]").text
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, cont_id=cont_id))
        return list(self.contact_cache)
