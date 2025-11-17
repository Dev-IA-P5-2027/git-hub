import csv


liste = []

def ma_liste(objet: str):
    liste.append(objet)
    return liste

def enlever(objet):
    liste.remove(objet)

def afficher():
    print(liste)

# def sauveguarder():
#     with open('liste.csv', 'w', newline='', encoding='utf-8') as fichier_csv:
#     liste = csv.writer(fichier_csv)
#     liste.writerows(lignes)
import csv

def sauvegarder(liste):
    with open('liste.csv', 'w', newline='', encoding='utf-8') as fichier_csv:
        writer = csv.writer(fichier_csv)
        writer.writerows(liste)


ma_liste("abricot")
print(liste)
sauvegarder(liste)


print("Bonjour choisisser parmis les solution suivante :")
print("1.ajouter un objet à ma liste \n 2.enlever un objet de ma liste \n 3.afficher ma liste \n 4.sauveguer ma liste")
