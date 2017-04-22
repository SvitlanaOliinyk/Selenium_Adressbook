

def test_delete_group(app):

    app.open_group_page()
    app.delete_group_by_number(0)
    # Verification
    assert 'Group has been removed.' in app.message()
    app.return_to_group_page()
    # TODO: Verify deletion group in list