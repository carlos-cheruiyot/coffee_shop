class Coffee:
    all_coffees = []

    def __init__(self, name):
        self.name = name
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be at least 3 characters long.")
