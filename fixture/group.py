

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

    def fill_group_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()

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
