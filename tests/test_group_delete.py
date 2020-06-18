# -*- coding: utf-8 -*-
from model.group_model import Group




def test_delete_first_group(app):
    app.session.login(name='admin', password='secret')
    app.group.delete_first_group()
    app.session.logout()