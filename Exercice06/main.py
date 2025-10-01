# Fonction calculate_average
# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50, "txt"]


def calculate_average(list_ : list[float]) -> float:
    """
    La founction permet de calculer la moyenne des nombre d'une liste

    Args:
        list_ (list(float)): lite de nombre au format float

    Returns:
        (float): Return la moyenne des nombres de la liste
    """
    moyenne = 0
    compteur = 0

    for nbr_ in list_:
        moyenne += nbr_
        compteur += 1

    moyenne = moyenne/compteur

    return moyenne


average = calculate_average(numbers)

print("La moyenne est :", average)
