from model.group import Group


def test_group(app):
    test_data_group = Group(name='Client', header='SuperHead', footer='Супер')
    app.open_group_page()
    app.create_group(test_data_group)
    # Verification
    assert 'A new group has been entered into the address book.' in app.message()
    app.return_to_group_page()
    # TODO: Verify group in grouplist

