import pytest
import random


@pytest.fixture(params=[0, 'random', -1], ids=['first', 'random', 'last'])
def index(app, request):
    if request.param == 'random':
        return random.randrange(1, app.group.count())
    return request.param


def test_delete_group(app, init_login, init_group, index, db):

    app.group.open_group_page()
    old_groups = db.get_group_list()
    app.group.delete_by_number(index)
    # Verification
    assert 'Group has been removed.' in app.message()
    app.group.return_to_group_page()
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    #Проверяем ,что удалился именно тот эл, который мы хотели
    old_groups.pop(index)
    assert old_groups == new_groups

