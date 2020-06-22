
from model.contact_model import Contact

def test_contact_edit(app):
    app.session.login(name='admin', password='secret')
    app.contact.delete_first_contact()
    app.session.logout()

