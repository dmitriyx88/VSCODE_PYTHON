"""Konstruktor classov"""


class Persons:
    """Test class"""
    def __init__(self, user_id, user_name):
        """Konstruktor"""
        self.user_id=user_id
        self.user_name=user_name
        self.text="Унаследованный атрибут"


class PersonsPhone(Persons):
    """Add phone"""
    def __init__(self, user_id, user_name, user_phone):
        "Add constr"
        Persons.__init__(self, user_id, user_name)
        self.user_phone= user_phone


x=Persons(123, "Dimon")
y=PersonsPhone(1234, "Toge Dimon", "34453")
print(y.user_name)
print(y.text)
