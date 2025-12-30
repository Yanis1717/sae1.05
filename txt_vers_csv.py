import csv
import re
import os

# On se place dans le bon dossier
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def generer_csv_propre():
    with open('DumpFile.txt', 'r') as f:
        lignes = f.readlines()

    with open('Analyse_Reseau.csv', 'w', newline='') as f_csv:
        writer = csv.writer(f_csv, delimiter=';')
        writer.writerow(['Heure', 'Source', 'Destination', 'Info_Paquet'])

        for ligne in lignes:
            # On ne prend que les lignes qui contiennent "IP" (les en-têtes de paquets)
            if "IP" in ligne:
                # On découpe la ligne par espaces
                elements = ligne.split()
                
                heure = elements[0]
                source = elements[2]
                destination = elements[4].replace(':', '') # On enlève le ":" à la fin
                # Le reste de la ligne contient les infos (Flags, seq, ack...)
                infos = " ".join(elements[5:])
                
                writer.writerow([heure, source, destination, infos])

generer_csv_propre()
print("Fichier Analyse_Reseau.csv créé ! Ouvrez-le avec Excel.")
