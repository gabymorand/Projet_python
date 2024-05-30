import os
import time

def mesurer_temps(fonction):
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        fin = time.time()
        temps_execution = fin - debut
        log_message = f"La fonction {fonction.__name__} a mis {temps_execution:.4f} secondes pour s'exécuter.\n"
        with open("logAdmin.log", "a") as f:
            f.write(log_message)
        print(log_message)
        return resultat
    return wrapper

def lire_fichier_journal(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        contenu = fichier.read()
    return contenu

def analyser_fichier_journal(contenu):
    lignes = contenu.split('\n')
    nombre_total_actions = 0
    statistiques_par_action = {}
    nombre_total_errors = 0
    statistiques_par_error = {}

    for ligne in lignes:
        if "ACTION:" in ligne:
            nombre_total_actions += 1
            action = ligne.split("ACTION:")[1].split('-')[0].strip()
            statistiques_par_action[action] = statistiques_par_action.get(action, 0) + 1
        elif "ERROR:" in ligne:
            nombre_total_errors += 1
            error = ligne.split("ERROR:")[1].split('-')[0].strip()
            statistiques_par_error[error] = statistiques_par_error.get(error, 0) + 1

    return nombre_total_actions, statistiques_par_action, nombre_total_errors, statistiques_par_error

def menu_principal():
    print("1. Choisir les fichiers à analyser")
    print("2. Quitter")

    option_menu_principal = input("Choisissez une option (1 ou 2): ")

    if option_menu_principal == '1':
        print("Option choisie dans le menu principal: 1\n")
        dossier_logs = "logs"
        fichiers_logs = [f for f in os.listdir(dossier_logs) if f.endswith(".log")]
        print("Liste des fichiers logs disponibles:")
        for i, fichier in enumerate(fichiers_logs, start=1):
            print(f"{i}. {fichier}")

        choix_fichiers = input("Choisissez les fichiers à analyser (séparés par des virgules, ex. 1,2): ")
        fichiers_a_analyser = [fichiers_logs[int(i) - 1] for i in choix_fichiers.split(',')]

        for fichier in fichiers_a_analyser:
            chemin_fichier = os.path.join(dossier_logs, fichier)
            contenu_fichier = lire_fichier_journal(chemin_fichier)
            log_message = f"\nAnalyse du fichier {fichier}\n"
            with open("logAdmin.log", "a") as f:
                f.write(log_message)
            print(log_message)
            
            @mesurer_temps
            def analyse_fichier():
                return analyser_fichier_journal(contenu_fichier)
            
            nombre_total, statistiques_actions, nombre_errors, statistiques_errors = analyse_fichier()
            
            log_message = f"Nombre total d'actions : {nombre_total}\n"
            with open("logAdmin.log", "a") as f:
                f.write(log_message)
            print(log_message)

            log_message = "Statistiques par type d'action:\n"
            for action, occurrences in statistiques_actions.items():
                log_message += f"{action} : {occurrences} occurrences\n"
            with open("logAdmin.log", "a") as f:
                f.write(log_message)
            print(log_message)

            log_message = f"\nNombre total d'erreurs : {nombre_errors}\n"
            with open("logAdmin.log", "a") as f:
                f.write(log_message)
            print(log_message)

            log_message = "Statistiques par type d'erreur:\n"
            for error, occurrences in statistiques_errors.items():
                log_message += f"{error} : {occurrences} occurrences\n"
            with open("logAdmin.log", "a") as f:
                f.write(log_message)
            print(log_message)

    elif option_menu_principal == '2':
        print("Option choisie dans le menu principal: 2")
        print("Programme terminé. Au revoir et merci!")
        exit()
    else:
        print("Option non valide. Veuillez choisir 1 ou 2.")

if __name__ == "__main__":
    menu_principal()
