# -*- coding: utf-8 -*-
from random import randrange

from model.group_model import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="firstGROUP"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))

    app.group.delete_group_by_index(index)
    new_group = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_group)
    old_groups[index:index+1] = []
    assert old_groups == new_group

