# Écrivez votre code ici !


def square(nbr_ : float) -> float:
    """
    La founction permet de calculer le carré de nbr_

    Args:
        nbr_ (float): nombre dont on calcul le carré

    Returns:
        (float): Return le carré de nbr_
    """

    if isinstance(nbr_,(int,float) ):
        carre = nbr_ * nbr_
        return carre
    else:
        raise TypeError("Attention le format de nbr_ n'est pas valide, utilisez un int ou un float")


nbr_calcul = input("Entrez le nombre à calculer :  ").strip()
# calcul = square(float(nbr_calcul))

# print(f"Le carre de {nbr_calcul} et de {calcul}")

try:
    nbr_calcul = float(nbr_calcul)   # conversion en float
    calcul = square(nbr_calcul)
    print(f"Le carré de {nbr_calcul} est {calcul}")
except ValueError:
    print("Erreur : vous devez entrer un nombre valide.")
except TypeError as e:
    print(e)
