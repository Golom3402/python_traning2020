# -*- coding: utf-8 -*-

from model.group_model import Group


def test_add_new_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    # group = Group(name="first_group", header="GROUP", footer="footer group")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)



