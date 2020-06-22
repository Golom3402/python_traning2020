from model.group_model import Group


def test_edit_group(app):
    app.session.login(name='admin', password='secret')
    app.group.edit('first_group', Group(name="second_group", header="GROUP222", footer="footer group4342"))
    app.session.logout()