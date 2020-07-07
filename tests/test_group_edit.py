from random import randrange

from model.group_model import Group


def test_edit_first_group(app):

    if app.group.count() == 0:
        app.group.create(Group(name="firstGROUP"))
    old_groups = app.group.get_group_list()
    group = Group(name="second_group", header="GROUP222", footer="footer group4342")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
