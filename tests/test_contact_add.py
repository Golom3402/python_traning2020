# -*- coding: utf-8 -*-
import pytest
from model.contact_model import Contact


def test_add_new_contact(app, json_contacts):
    contact = json_contacts
    old_list = app.contact.get_contact_list()
    app.open_home_page()
    app.contact.add_new(contact=contact)
    app.return_to_home_page()
    assert len(old_list) + 1 == app.contact.count()
    new_list = app.contact.get_contact_list()
    old_list.append(contact)
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)
