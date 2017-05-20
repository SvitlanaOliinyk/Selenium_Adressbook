from  pytest_bdd import given, then, when, scenario
from model.group import Group


@scenario('group.feature', 'Add new group')
def test_add_new_group():
    pass

@given("a group list")
def old_groups(db):
    return db.get_group_list()

@given("a group with <name>, <header>, <footer>")
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when("I add a new group to the list")
def add_new_group(app, init_login, name, header, footer):
    app.group.open_group_page()
    app.group.create(Group(name=name, header=header, footer=footer))
    app.group.return_to_group_page()

@then("a new group list is equal to the old list with the old group")
def verify_group_adding(db, old_groups, new_group):
    new_groups_list = db.get_group_list()
    assert len(old_groups) + 1 == len(new_groups_list)
    old_groups.append(new_group)
    assert sorted(old_groups) == sorted(new_groups_list)