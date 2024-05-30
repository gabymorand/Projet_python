import random
def choisir_mot():
    liste_mots = ["python", "programmation", "pendu", "informatique", "jeu"]
    return random.choice(liste_mots)
def afficher_mot_cache(mot, lettres_trouvees):
    mot_affiche = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_affiche += lettre
        else:
            mot_affiche += "_"
    return mot_affiche
def jouer_pendu():
    mot_a_deviner = choisir_mot().lower()
    lettres_trouvees = set()
    essais_max = 6
    essais = 0
    print("Bienvenue au jeu du pendu!")
    while essais < essais_max:
        mot_affiche = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
        print("\nMot à deviner : " + mot_affiche)
        if mot_affiche == mot_a_deviner:
            print("Félicitations! Vous avez deviné le mot!")
            break
        lettre = input("Devinez une lettre : ").lower()
        if lettre in lettres_trouvees:
            print("Vous avez déjà deviné cette lettre. Essayez à nouveau.")
            continue
        if lettre in mot_a_deviner:
            lettres_trouvees.add(lettre)
            print("Bonne devinette!")
        else:
            essais += 1
            print("Incorrect! Essais restants : {}".format(essais_max - essais))
    if essais == essais_max:
        print("Désolé, vous avez atteint le nombre maximum d'essais. Le mot était '{}'.".format(mot_a_deviner))
if __name__ == "__main__":
    jouer_pendu()
