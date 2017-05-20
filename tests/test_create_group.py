
# @pytest.mark.parametrize('test_data_group', test_groups, ids=[repr(el) for el in test_groups]
def test_group(app, init_login, test_groups, db):
    app.group.open_group_page()
    old_groups = db.get_group_list()
    app.group.create(test_groups)
    # Verification
    assert 'A new group has been entered into the address book.' in app.message()
    app.group.return_to_group_page()
    # TODO: Verify group in grouplist
    new_groups = db.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(test_groups)
    assert sorted(old_groups) == sorted(new_groups)


