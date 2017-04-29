

def test_delete_group(app, init_login, init_group):

    app.group.open_group_page()
    old_groups = app.group.get_list()
    app.group.delete_by_number(0)
    # Verification
    assert 'Group has been removed.' in app.message()
    app.group.return_to_group_page()
    # TODO: Verify deletion group in list
    new_group = app.group.get_list()
    assert len(old_groups) - 1 == len(new_group)

