# -*- coding: utf-8 -*-
import string
from sys import maxsize
import pytest
import random
import string
from model.group_model import Group
from data.groups import testdata


def test_add_new_group(app, data_groups):
    group = data_groups
    old_groups = app.group.get_group_list()
    # group = Group(name="first_group", header="GROUP", footer="footer group")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)


# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_group = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_group)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)



