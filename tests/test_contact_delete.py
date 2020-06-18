
from model.contact_model import Contact

def test_contact_edit(app):
    app.session.login(name='admin', password='secret')
    old_contact=Contact(first_name='Test_user1', middle_name='Петрович', last_name="Ватутин", nickname="Test1")
    app.contact.delete(contact=old_contact)
    app.session.logout()

