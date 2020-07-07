from random import randrange

from model.contact_model import Contact

def test_contact_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(first_name='Test_user1', middle_name='Петрович', last_name="Ватутин", nickname="Test1"))
    old_list = app.contact.get_contact_list()
    new_contact = Contact(
        first_name='Нестор', middle_name='Петрович', last_name="Ложкин", nickname="Test1113")
    index = randrange(len(old_list))
    new_contact.cont_id = old_list[index].cont_id
    app.contact.edit_contact_by_index(index, new_contact=new_contact)
    new_list = app.contact.get_contact_list()
    old_list[index] = new_contact
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)
