import csv
import json


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

def sauvegarder(liste):
    with open(r"C:\Users\jesse.richard\Desktop\git-hub\liste.json", "w", encoding="utf-8") as f:
        json.dump(liste, f, ensure_ascii=False, indent=4)

while True:
    print("Bonjour choisisser parmis les solution suivante :")
    print("1.ajouter un objet à ma liste \n 2.enlever un objet de ma liste \n 3.afficher ma liste \n 4.sauveguer ma liste \n 5.quitter" )
    n = int(input("Entre ta solution"))
    if n == 1:
        objet = input("Entre le nom du produit que tu veux ajoutez")
        ma_liste(objet)
    if n == 2:
        objet = input("Entre le nom du produit que tu veux retirer")
        enlever(objet)
    if n == 3:
        afficher()
    if n == 4:
        sauvegarder(liste)
    if n == 5:
        break
