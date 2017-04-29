from model.group import Group


def test_group(app, init_login):
    test_data_group = Group(name='Client', header='SuperHead', footer='Супер')
    app.group.open_group_page()
    app.group.create(test_data_group)
    # Verification
    assert 'A new group has been entered into the address book.' in app.message()
    app.group.return_to_group_page()
    # TODO: Verify group in grouplist

