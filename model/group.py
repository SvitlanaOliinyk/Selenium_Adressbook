

class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self): #Как отображать группу
        return 'id: {}, name: {}, header: {}, footer: {}'.format(self.id, self.name, self.header, self.footer)

    def __eq__(self, other):  #Сравнивание на равенство
        if self.id is None or other.id is None:
            return self.name == other.name
        else:
            return self.id == other.id and self.name == other.name

    def __lt__(self, other):
        #Так как мы не знаем айдишник новой созданной группы, то принудительно сделаем, что
        # None - это максимальное значение
        if self.id is None:
            return False
        elif other.id is None:
            return True
        return self.id < other.id
