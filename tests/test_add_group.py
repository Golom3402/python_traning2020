# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group_model import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.session.login(name='admin', password='secret')
    app.group.create(Group(name="first_group", header="GROUP", footer="footer group"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(name='admin', password='secret')
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


