# Écrivez votre code ici !


class Person:
    """
    Classe représentant une Person.

    Attributs:
        name (str): nom de la personne.
        age (int): age de la personne.

    Méthodes:
        display_details(): Affiche les attribut de Person
    """

    def __init__(self, name:str, age:int):
        """
        Initialise une instance de la classe Rectangle.

        Args:
            name (str): nom de la personne.
            age (int): age de la personne.
        """
        self.name = name
        self.age = age

    def display_details(self) -> None:
        """Affiche les détails de la personne (nom et âge)."""
        Person.common_display(self.name, self.age)

    @staticmethod
    def common_display(name: str, age: int) -> None:  # possiblité d'utilsier **kwarg pour une liste indeterminé.
        """
        Méthode statique commune qui affiche un nom et un âge.
        Utilisable aussi bien par Person que par Employee.
        """
        print(f"Nom: {name}, Âge: {age}")


class Employee(Person):
    """
    Classe représentant un employé, héritant de Person.

    Attributs supplémentaires:
        salary (float): Salaire de l'employé.
    """

    def __init__(self, name: str, age: int, salary: float):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self) -> None:
        """Affiche les détails de l'employé (nom, âge et salaire)."""
        # on réutilise la méthode statique commune
        Person.common_display(self.name, self.age)
        print(f"Salaire: {self.salary}")


# #-----------------------------------------

# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def display_details(self) -> None:
#         Person.common_display(name=self.name, age=self.age)

#     @staticmethod
#     def common_display(**kwargs) -> None:
#         """
#         Méthode statique commune qui affiche les détails
#         passés en arguments sous forme clé=valeur.
#         """
#         details = ", ".join(f"{cle.capitalize()}: {val}" for cle, val in kwargs.items())
#         print(details)


# class Employee(Person):
#     def __init__(self, name: str, age: int, salary: float):
#         super().__init__(name, age)
#         self.salary = salary

#     def display_details(self) -> None:
#         Person.common_display(name=self.name, age=self.age, salaire=self.salary)

p = Person("Alice", 30)
p.display_details()

e = Employee("Bob", 40, 3500.0)
e.display_details()