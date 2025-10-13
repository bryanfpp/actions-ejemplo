class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name.title()} {self.last_name.title()}"


if __name__ == "__main__":
    p1 = Person("juan", "perez")
    p2 = Person("MARIA", "LOPEZ")
    p3 = Person("cArLoS", "gOnZaLeZ")
    
    print(p1)  # Juan Perez
    print(p2)  # Maria Lopez
    print(p3)  # Carlos Gonzalez
