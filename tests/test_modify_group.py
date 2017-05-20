from model.group import Group
import pytest
from data.test_groups import test_groups


@pytest.mark.parametrize('index', [0, -1], ids=['first', 'last'])
@pytest.mark.parametrize('test_data_group', test_groups, ids=[repr(el) for el in test_groups])
def test_modify_by_number(app, init_login, init_group, index):
    data_to_modify = Group(name='dfkjldkfj')
    app.group.open_group_page()
    old_groups = app.group.get_list()
    app.group.modify_by_number(index, data_to_modify)
    # Verification
    assert 'Group record has been updated.' in app.message()
    app.group.return_to_group_page()

    new_groups = app.group.get_list()
    assert len(old_groups) == len(new_groups)
    #В элементе, который изменяли, в старом списке вносим изменения (только в заполненные поля!)
    if data_to_modify.name is not None:
        old_groups[index].name = data_to_modify.name
    assert sorted(old_groups) == sorted(new_groups)