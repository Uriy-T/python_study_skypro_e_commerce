class InitObject:

    def __init__(self):
        print(self.__repr__())


    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([str(value) for value in self.__dict__.values()])})"
