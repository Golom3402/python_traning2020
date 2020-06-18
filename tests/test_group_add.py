# -*- coding: utf-8 -*-
from model.group_model import Group

def test_add_new_group(app):
    app.session.login(name='admin', password='secret')
    app.group.create(Group(name="first_group", header="GROUP", footer="footer group"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(name='admin', password='secret')
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


