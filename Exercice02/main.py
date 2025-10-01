from tabulate import tabulate

students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

name = input("Entrez le nom de l’étudiant :  ").strip().capitalize()
moyen = 0

if name in students:
    print(f"Notes de {name} :")
    for matiere in students[name]:
        notes = students[name][matiere]
        print(f"     {matiere} : {notes}")
        moyen = notes + moyen

    moyen = round((moyen / 3), 2)
    print(f"La moyenne de {name} est de {moyen}\n")
    # Préparer les données pour tabulate
    tableau_note = [[matiere, note] for matiere, note in students[name].items()]
    tableau_note.append(["moyen",moyen])
    # Afficher le tableau formaté
    print(tabulate(tableau_note, headers=["Matière", "Note"], tablefmt="grid"))
    print()

else:
    print("Étudiant non trouvé.")