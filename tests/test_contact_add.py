# -*- coding: utf-8 -*-
import pytest
from model.contact_model import Contact


def test_add_new_contact(app, data_contacts):
    contact = data_contacts
    old_list = app.contact.get_contact_list()
    # contact = Contact(first_name='Test_user1', middle_name='Петрович', last_name="Ватутин", nickname="Test1",
    #                   photo="C:\\fakepath\\Koala.jpg", title='TutleTest data1', company='E-corp',
    #                   address='York sheer 13',
    #                   home_tel='+3-9-99-99-9-9-9', work_tel='+7-495-399-59-59', mobile_tel='+79291929929',
    #                   fax='3334528',
    #                   email='petrovi4@mail.ru', email2='test1@yandex.ru', email3='vatutin123@gmail.com',
    #                   homepage='www.facebook.com', b_day='14', b_month='December', b_year='1944', anny_day='14',
    #                   anny_month='April', anny_year='1994', group=None, address2='address 2 2 2', phone2='123456789-0',
    #                   notes='notes notes notes notes notes notes notes notes notes notes notes notes notes notes')
    app.open_home_page()
    app.contact.add_new(contact=contact)
    app.return_to_home_page()
    assert len(old_list) + 1 == app.contact.count()
    new_list = app.contact.get_contact_list()
    old_list.append(contact)
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)
