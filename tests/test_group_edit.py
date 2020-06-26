from model.group_model import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="second_group", header="GROUP222", footer="footer group4342"))

def test_edit_target_group(app):
    app.group.edit(old_name="first_group", new_group=Group(name="second_group",
                                                           header="GROUP222", footer="footer group4342"))
