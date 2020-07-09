import re
from random import randrange


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_tel == contact_from_edit_page.home_tel
    assert contact_from_view_page.mobile_tel == contact_from_edit_page.mobile_tel
    assert contact_from_view_page.work_tel == contact_from_edit_page.work_tel
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def test_all_data_on_home_page(app):
    count = app.contact.count()
    index = randrange(count)
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert clear(contact_from_home_page.last_name) == clear(contact_from_home_page.last_name)
    assert clear(contact_from_home_page.first_name) == clear(contact_from_home_page.first_name)
    assert clear(contact_from_home_page.address) == clear(contact_from_home_page.address)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)




def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    result =  "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_tel, contact.mobile_tel, contact.work_tel, contact.phone2]))))
    return  result

def merge_emails_like_on_home_page(cont):
    result = "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,[cont.email, cont.email2, cont.email3]))))
    return result