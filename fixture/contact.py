from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
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
        wd = self.app.wd
        wd.find_element_by_name(text_field).click()
        wd.find_element_by_name(text_field).clear()
        wd.find_element_by_name(text_field).send_keys(text)

    def choose_text_in_drop_down_list_by_name(self, field_name, text):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
        wd.find_element_by_name(field_name).click()