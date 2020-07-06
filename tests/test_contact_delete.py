
from model.contact_model import Contact

def test_contact_delete(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(first_name='first_contact', last_name="Голубков"))
    old_list = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_list = app.contact.get_contact_list()
    assert len(old_list) - 1 == len(new_list)
    old_list[0:1] = []
    assert old_list == new_list


