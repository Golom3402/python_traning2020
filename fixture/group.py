from model.group_model import Group


class GroupHelper():
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        # return to groups
        # wd.find_element_by_link_text("groups").click()
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        # init group creation
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # supbit
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.fill_text_field_by_name(text_field="group_name", text= group.name)
        self.fill_text_field_by_name(text_field="group_header", text=group.header)
        self.fill_text_field_by_name(text_field="group_footer", text=group.footer)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name('new')) > 0):
            wd.find_element_by_link_text("groups").click()

    def count(self):
        wd=self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name('selected[]'))


    def edit(self, old_name, new_group):
        """
        :param old_name:  str имя группы, которую нужно отредактировать
        :param new_group: объект класса Group, с новыми значениями
        :return:
        """
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_xpath(f'//span[text()="{old_name}"]/input').click()
        wd.find_element_by_name('edit').click()
        self.fill_group_form(new_group)
        wd.find_element_by_name('update').click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_first_group(self, new_group):
        self.edit_group_by_index(0, new_group)

    def edit_group_by_index(self, index, new_group):
        """
        :param index: номер группы в списке групп, который будем изменять
        :param new_group: объект класса Group, с новыми значениями
        :return:
        """
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name('edit').click()
        self.fill_group_form(new_group)
        wd.find_element_by_name('update').click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_text_field_by_name(self, text_field, text):
        wd = self.app.wd
        if text:
            wd.find_element_by_name(text_field).click()
            wd.find_element_by_name(text_field).clear()
            wd.find_element_by_name(text_field).send_keys(text)
        else:
            pass

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache=[]
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()