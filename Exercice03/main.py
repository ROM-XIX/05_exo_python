words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
mot = "aeiouyAEIOUY"
list = []

for words_ in words :
    compteur = 0
    #print(f"{words_}")

    for lettre in words_:
        if lettre in mot:
            compteur += 1

    list.append((words_,compteur))    

print(f"{list}")
#    print(f"Le mot '{words_}' contient {compteur} voyelle(s).")