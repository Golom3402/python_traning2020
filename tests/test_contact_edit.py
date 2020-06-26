
from model.contact_model import Contact

def test_contact_edit_first_contact(app):
    new_contact = Contact(
        first_name='Нестор', middle_name='Петрович', last_name="Ложкин", nickname="Test1113")
    app.contact.edit_first_contact(new_contact=new_contact)


def test_contact_edit(app):
    old_contact=Contact(first_name='Test_user1', middle_name='Петрович', last_name="Ватутин", nickname="Test1")
    new_contact=Contact(
        first_name='Нестор', middle_name='Петрович', last_name="Ложкин", nickname="Test1",
        photo="C:\\fakepath\\Koala.jpg", title='TutleTest data1', company='E-corp',
        address='York sheer 13',
        home_tel='+3-7777777777777', work_tel='+7-433 457 5729', mobile_tel='+79291929929',
        fax='3334528',
        email='petrovi4@mail.ru', email2='test1@yandex.ru', email3='vatutin123@gmail.com',
        homepage='www.facebook.com', b_day='14', b_month='December', b_year='1944', anny_day='14',
        anny_month='April', anny_year='1994', group=None, address2='address 2 2 2', phone2='123456789-0',
        notes='notes notes notes notes notes notes notes notes notes notes notes notes notes notes'
    )
    app.contact.edit(old_contact=old_contact, new_contact=new_contact)


