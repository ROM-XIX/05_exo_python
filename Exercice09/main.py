class Rectangle:
    """
    Classe représentant un Rectangle.

    Attributs:
        length (int): longueur du rectangle.
        width (int): largeur du rectangle.

    Méthodes:
        calculate_area(): Calcule l'aire du rectangle.
        calculate_perimeter(): Calcule du périmètre du rectangle
    """

    def __init__(self, length, width):
        """
        Initialise une instance de la classe Rectangle.

        Args:
            length (int): longueur du rectangle.
            width (int): largeur du rectangle.
        """
        self.length = length
        self.width = width

    def calculate_area(self):
        """Calcul de l'aire du rectangle."""
        area = self.length * self.width
        return area

    def calculate_perimeter(self):
        """Calcul du perimètre du rectangle."""       
        perimetre = 2 * self.length + 2 * self.width
        return perimetre


# Test de la classe Rectangle
rectangle = Rectangle(5, 3)  # 5:width & 3:length
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area())
print("Périmètre:", rectangle.calculate_perimeter())
