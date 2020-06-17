# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact_model import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.open_home_page()
    app.login(name='admin', password='secret')
    contact = Contact(first_name='Test_user1', middle_name='Петрович', last_name="Ватутин", nickname="Test1",
                      photo="C:\\fakepath\\Koala.jpg", title='TutleTest data1', company='E-corp',
                      address='York sheer 13',
                      home_tel='+3-9-99-99-9-9-9', work_tel='+7-495-399-59-59', mobile_tel='+79291929929',
                      fax='3334528',
                      email='petrovi4@mail.ru', email2='test1@yandex.ru', email3='vatutin123@gmail.com',
                      homepage='www.facebook.com', b_day='14', b_month='December', b_year='1944', anny_day='14',
                      anny_month='April', anny_year='1994', group=None, address2='address 2 2 2', phone2='123456789-0',
                      notes='notes notes notes notes notes notes notes notes notes notes notes notes notes notes')
    app.open_home_page()
    app.add_new_contact(contact=contact)
    app.return_to_home_page()
