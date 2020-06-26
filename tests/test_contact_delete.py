
from model.contact_model import Contact

def test_contact_delete(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(first_name='first_contact', last_name="Голубков"))
    app.contact.delete_first_contact()


