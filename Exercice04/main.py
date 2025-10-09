class MyClass:
    def __init__(self, full_name):
        self.full_name = full_name

    def displayName(self):
        print("Le nom complet est :", self.full_name)


class Other_Class:
    def __init__(self, first_name, name):
        self.first_name = first_name
        self.name = name

    def display_name(self):
        print(f"Nom complet : {self.first_name} {self.name}")
