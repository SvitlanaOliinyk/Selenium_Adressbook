import random
import string
from model.group import Group
import json
import os.path

def random_string(maxlen):
    lenght = random.randrange(maxlen)
    synbols = string.ascii_letters + ' '*10 + string.digits #+ string.punctuation
    return ''.join([random.choice(synbols) for _ in range(lenght)])

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),"group_data.json")

with open(file_name, encoding='utf&') as f:
    test_groups = [Group(**data) for data in json.load(f)]

test_groups += [
    Group(name=random_string(10), header=random_string(50), footer=random_string(50))
    for _ in range(2)
]

# test_groups = [
#     Group(name=random_string(10), header=random_string(5), footer=random_string(5))
# ]


# names = ['', random_string(3)]
# headers = ['', 'sd']
# footers = ['', 'sd']
#
# test_groups = [
#     Group(name=name, header=header, footer=footer)
#     for name in names
#     for header in headers
#     for footer in footers
# ]


# test_groups = [
#     Group(name='dfsdfdf', header='sdgfsdf', footer='dfgdfg'),
#     Group(name='124124', header='123123', footer='23141234'),
#     Group(name='впаыва', header='пукпвап', footer='впвпвкп')
# ]