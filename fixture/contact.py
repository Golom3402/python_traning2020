import time
import re
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
        self.open_contact_by_index(index)
        self.fill_contact_form(new_contact)
        wd.find_element_by_name('update').click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def open_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        locator = '//td/a/img[@title="Edit"]'
        edit_buttons = wd.find_elements_by_xpath(locator)
        edit_buttons[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.click()

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
                address = element.find_element_by_xpath("./td[4]").text
                all_phones = element.find_element_by_xpath("./td[6]").text
                all_emails = element.find_element_by_xpath("./td[5]").text
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, cont_id=cont_id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_by_index(index)
        wd = self.app.wd

        contact = Contact()
        contact.first_name = wd.find_element_by_name('firstname').get_attribute("value")
        contact.middle_name = wd.find_element_by_name('middlename').get_attribute("value")
        contact.last_name = wd.find_element_by_name('lastname').get_attribute("value")
        contact.nickname = wd.find_element_by_name('nickname').get_attribute("value")
        contact.title = wd.find_element_by_name('title').get_attribute("value")
        contact.company = wd.find_element_by_name('company').get_attribute("value")
        contact.address = wd.find_element_by_name('address').get_attribute("value")
        contact.home_tel = wd.find_element_by_name('home').get_attribute("value")
        contact.mobile_tel = wd.find_element_by_name('mobile').get_attribute("value")
        contact.work_tel = wd.find_element_by_name('work').get_attribute("value")
        contact.fax = wd.find_element_by_name('fax').get_attribute("value")
        contact.email = wd.find_element_by_name('email').get_attribute("value")
        contact.email2 = wd.find_element_by_name('email2').get_attribute("value")
        contact.email3 = wd.find_element_by_name('email3').get_attribute("value")
        contact.homepage = wd.find_element_by_name('homepage').get_attribute("value")
        contact.b_day = wd.find_element_by_name('bday').get_attribute("value")
        contact.b_month = wd.find_element_by_name('bmonth').get_attribute("value")
        contact.b_year = wd.find_element_by_name('byear').get_attribute("value")
        contact.anny_day = wd.find_element_by_name('aday').get_attribute("value")
        contact.anny_month = wd.find_element_by_name('amonth').get_attribute("value")
        contact.anny_year = wd.find_element_by_name('ayear').get_attribute("value")
        # if contact.group:
        #     self.choose_text_in_drop_down_list_by_name('new_group', contact.group)
        contact.address2 = wd.find_element_by_name('address2').get_attribute("value")
        contact.phone2 = wd.find_element_by_name('phone2').get_attribute("value")
        contact.notes = wd.find_element_by_name('notes').get_attribute("value")
        contact.cont_id = wd.find_element_by_name('id').get_attribute("value")
        return contact

    def get_contact_from_view_page(self, index):
        wd = self.app.wd

        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_tel = re.search("H: (.*)", text).group(1)
        work_tel = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        mobile_tel = re.search("M: (.*)", text).group(1)
