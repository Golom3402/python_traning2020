from random import randrange

from model.contact_model import Contact

def test_contact_delete(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(first_name='first_contact', last_name="Голубков"))
    old_list = app.contact.get_contact_list()
    index = randrange(len(old_list))
    app.contact.delete_contact_by_index(index)
    new_list = app.contact.get_contact_list()
    assert len(old_list) - 1 == len(new_list)
    old_list[index:index+1] = []
    assert old_list == new_list


