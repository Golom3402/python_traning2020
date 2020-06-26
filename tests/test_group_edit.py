from model.group_model import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="firstGROUP"))
    app.group.edit_first_group(Group(name="second_group", header="GROUP222", footer="footer group4342"))
