
from model.contact_model import Contact

def test_contact_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(first_name='Test_user1', middle_name='Петрович', last_name="Ватутин", nickname="Test1"))
    new_contact = Contact(
        first_name='Нестор', middle_name='Петрович', last_name="Ложкин", nickname="Test1113")
    app.contact.edit_first_contact(new_contact=new_contact)

