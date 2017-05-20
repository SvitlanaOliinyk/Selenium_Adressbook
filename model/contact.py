

class Contact:
    def __init__(self, id=None, firstname=None, middlename=None, lastname=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.id = id


    def __repr__(self): #Как отображать группу
        return 'id: {}, firstname: {}, middlename: {}, lastname: {}'.format(self.id, self.firstname, self.middlename, self.lastname)

    # def __eq__(self, other):  #Сравнивание на равенство
    #     if self.id is None or other.id is None:
    #         return self.name == other.name
    #     else:
    #         return self.id == other.id and self.name == other.name
    #
    # def __lt__(self, other):
    #     #Так как мы не знаем айдишник новой созданной группы, то принудительно сделаем, что
    #     # None - это максимальное значение
    #     if self.id is None:
    #         return False
    #     elif other.id is None:
    #         return True
    #     return self.id < other.id
