LISTE_COURS = ["Mathematiques", "Physique", "Chimie", "Biologie", "Histoire"]


#Initialise la classe etudiant 
#A note que la liste_cours sert principalement a initialsé de base la listes des cours.
class Etudiant:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.notes = {cours: [] for cours in LISTE_COURS}

#Ajoute une note dans un cours
    def ajouter_note(self, cours, note):
        if cours in self.notes and 0 <= note <= 20:
            self.notes[cours].append(note)
        else:
            print("\n Note invalide. Veuillez entrer une note entre 0 et 20.")

#Fait la moyenne de toute les notes
    def moyenne_totale(self):
        total = 0
        count = 0
        for notes in self.notes.values():
            total += sum(notes)
            count += len(notes)
        return total / count if count > 0 else 0

#Fait la moyenne d'un cours
    def moyenne_cours(self, cours):
        if cours in self.notes:
            return sum(self.notes[cours]) / len(self.notes[cours])
        else:
            return 0


class GestionNotes:
    def __init__(self):
        self.etudiants = []
#Permet d'ajouter un etudiant
    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

#Permet d'afficher les notes d'un etudiant pour un cour donné
    def afficher_notes_cours_etudiant(self, etudiant, cours):
        if cours in etudiant.notes:
            print("\n Notes de l'étudiant {} {} pour le cours {} :".format(etudiant.nom, etudiant.prenom, cours))
            notes_cours = etudiant.notes[cours]
            if notes_cours:
                print("{} : {}".format(cours, ', '.join(map(str, notes_cours))))
            else:
                print("\n Aucune note trouvée pour le cours {}.".format(cours))
        else:
            print(" \n Aucune note trouvée pour le cours {}.".format(cours))

#Permet d'afficher la moyenne total d'un etudiant
    def afficher_moyenne_totale_etudiant(self, etudiant):
        moyenne_totale = etudiant.moyenne_totale()
        print("\n Moyenne totale de l'étudiant {} {} : {:.2f}".format(etudiant.nom, etudiant.prenom, moyenne_totale))


#Permet d'afficher la moyenne total des etudiants
    def afficher_moyenne_totale(self):
        total_moyenne = 0
        count_etudiants = 0
        for etudiant in self.etudiants:
            total_moyenne += etudiant.moyenne_totale()
            count_etudiants += 1

        moyenne_totale = total_moyenne / count_etudiants if count_etudiants > 0 else 0
        print("\n Moyenne totale de tous les étudiants : {:.2f}".format(moyenne_totale))

#Permet d'afficher la moyenne d'un cours
    def afficher_moyenne_cours(self, cours):
        total_notes = 0
        count_etudiants = 0
        for etudiant in self.etudiants:
            if cours in etudiant.notes:
                total_notes += sum(etudiant.notes[cours])
                count_etudiants += len(etudiant.notes[cours])

        moyenne_cours = total_notes / count_etudiants if count_etudiants > 0 else 0
        print("\n Moyenne du cours {} : {:.2f}".format(cours, moyenne_cours))

    # Fonction secrète, affiche toute les notes d'un cours, utiliser pour le debug
    def afficher_toutes_les_notes(self, etudiant):
        print("\n Toutes les notes de l'étudiant {} {} :".format(etudiant.nom, etudiant.prenom))
        for cours, notes in etudiant.notes.items():
            print("{} : {}".format(cours, ', '.join(map(str, notes))))


#Afficher la liste des cours Disponibles 
    def afficher_liste_cours(self):
        print("\nListe des cours disponibles :")
        for cours in LISTE_COURS:
            print(cours)

#Fonction secrète, Permet d'ajouter un etudiant à tout les cours disponible et de fixé sa note
    def ajouter_etudiant_a_tous_les_cours(self, etudiant):
        for cours in LISTE_COURS:
            note = int(input("Note pour le cours {} (entre 0 et 20) : ".format(cours)))
            etudiant.ajouter_note(cours, note)
        self.ajouter_etudiant(etudiant)

    def afficher_menu(self):
        print('Menu Interactif :')
        print('1: Ajouter un élève à un cours avec une note dans ce cours')
        print('2: Afficher les notes dun élève pour un cours spécifique')
        print("3: Afficher la moyenne totale d'un élève.")
        print('4: Afficher la moyenne dun cours spécifique.')
        print('5: Afficher la moyenne totale de tous les élèves.')
        print('6: Quitter le programme.')
        print('7: Afficher la liste des cours disponibles.')
        print('8: Programme secret : Liste des notes de tous les étudiants pour un cours spécifique.')
        print('9: Programme secret : Ajouter un élève à tous les cours avec des notes entre 0 et 20.')

def quitter_programme():
    print("Programme terminé. Au revoir et merci!")
    exit()

if __name__ == "__main__":
    gestion_notes = GestionNotes()

    while True:
        gestion_notes.afficher_menu()
        choix = input("Choisissez une option (1-9) : ")

        match choix:
            case "1":
                nom = input("Nom de l'étudiant : ")
                prenom = input("Prénom de l'étudiant : ")
                etudiant = Etudiant(nom, prenom)
                cours = input("Nom du cours : ")
                note = int(input("Note (entre 0 et 20) : "))
                etudiant.ajouter_note(cours, note)
                gestion_notes.ajouter_etudiant(etudiant)
                print("\n Note ajoutée avec succès!")

            case "2":
                nom = input("Nom de l'étudiant : ")
                prenom = input("Prénom de l'étudiant : ")
                etudiant = next((e for e in gestion_notes.etudiants if e.nom == nom and e.prenom == prenom), None)
                if etudiant:
                    cours = input("Nom du cours : ")
                    gestion_notes.afficher_notes_cours_etudiant(etudiant, cours)
                else:
                    print("\n Étudiant non trouvé.")

            case "3":
                nom = input("Nom de l'étudiant : ")
                prenom = input("Prénom de l'étudiant : ")
                etudiant = next((e for e in gestion_notes.etudiants if e.nom == nom and e.prenom == prenom), None)
                if etudiant:
                    gestion_notes.afficher_moyenne_totale_etudiant(etudiant)
                else:
                    print("\n Étudiant non trouvé.")

            case "4":
                cours = input("Nom du cours : (Les cours existants sont : Mathematiques, Physique, Chimie, Biologie, Histoire]) :")
                gestion_notes.afficher_moyenne_cours(cours)

            case "5":
                gestion_notes.afficher_moyenne_totale()

            case "6":
                quitter_programme()

            case "7":
                gestion_notes.afficher_liste_cours()

            case "8":
                print("Programme secret : liste des notes de tous les étudiants pour un cours spécifique")
                cours = input("Nom du cours : ")
                for etudiant in gestion_notes.etudiants:
                    gestion_notes.afficher_notes_cours_etudiant(etudiant, cours)

            case "9":
                etudiant = Etudiant(input("Nom de l'étudiant : "), input("Prénom de l'étudiant : "))
                gestion_notes.ajouter_etudiant_a_tous_les_cours(etudiant)

            case _:
                print("\n Option invalide. Veuillez choisir une option de 1 à 9.")
