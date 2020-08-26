from bpylist import archiver

class Person:

    def __init__(self, name, age, house):
        self.name = name
        self.age = age
        self.house = house

    def __eq__(self, other):
        for field in ['name', 'age', 'house']:
            if getattr(self, field) != getattr(other, field):
                return False
        return True

    @staticmethod
    def encode_archive(obj, archive):
        archive.encode('name', obj.name)
        archive.encode('age', obj.age)
        archive.encode('house', obj.house)

    @staticmethod
    def decode_archive(archive):
        name = archive.decode('name')
        age = archive.decode('age')
        house = archive.decode('house')
        return Person(name, age, house)


archiver.update_class_map({'crap.Foo': Person})
obj = Person('herp', '42','strawberries')
archiver.archive(obj)