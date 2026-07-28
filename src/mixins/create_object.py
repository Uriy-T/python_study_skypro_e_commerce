class InitObject:

    def __init__(self) -> None:
        print(self.__repr__())

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"({', '.join([str(value) for value in self.__dict__.values()])})"
        )
