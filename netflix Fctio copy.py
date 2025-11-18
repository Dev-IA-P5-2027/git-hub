import pandas as pd
from ast import literal_eval
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ast

print(pd.__version__)

#--- importation ---

movies = pd.read_csv(r"C:\Users\jesse.richard\Desktop\Mes projets\Projet Python\data\movies_metadata.csv", sep = ",")
# movies = pd.read_csv(r"C:\Users\Jayso\Desktop\GitHub\Projet python\data\movies_metadata.csv", sep = ",")
# credits = pd.read_csv(r"C:\Users\jesse.richard\Desktop\Mes projets\Projet Python\credits.csv", sep = ",")
# credits = pd.read_csv(r"C:\Users\Jayso\Desktop\GitHub\Projet python\data\credits.csv", sep = ",")

#--- Génération des liste de Filtre à partir du CSV ---

def list_genres() -> list:
    # Lecture du fichier
    # movies = pd.read_csv(r"C:\Users\Jayso\Desktop\GitHub\Projet python\data\movies_metadata.csv", sep = ",", low_memory=False)
    movies = pd.read_csv(r"C:\Users\jesse.richard\Desktop\Mes projets\Projet Python\data\movies_metadata.csv", sep = ",", low_memory=False)

    genres_set = set()

    for entry in movies["genres"].dropna():
        try:
            # Convertit la chaîne JSON-like en objet Python
            genres_list = ast.literal_eval(entry)

            # Ajoute chaque genre dans l'ensemble
            for g in genres_list:
                genres_set.add(g["name"])
        except:
            pass  # ignore les lignes mal formatées

    return sorted(genres_set)

Liste_des_genres = list_genres()
print(Liste_des_genres)

#--- Dico dynamique ---

movies_metadata = ["adult", "belongs_to_collection", "budget","genres", "homepage", "id", "imdb_id", "original_language", "original_title", "overview",
"popularity", "poster_path", "production_companies", "production_countries", "release_date", "revenue", "runtime", "spoken_languages", "status", "tagline",
"title", "video", "vote_average", "vote_count"]

Film = {"movies_metadata" : 
          {"adult": [True, False],
          "belongs_to_collection" : [2],
          "budget" : [30000000, 65000000, 16000000],
          "genres" : Liste_des_genres, 
          "homepage" : [4],
          "id" : [5],
          "imdb_id" : [6],
          "original_language" : [7],
          "original_title" : [8],
          "overview" : [9],
          "popularity" : [10],
          "poster_path" : [11],
          "production_companies" : [12],
          "production_countries" : [14],
          "release_date" : [15],
          "revenue" : [16],
          "runtime" : [17],
          "spoken_languages" : [18],
          "status" : [19],
          "tagline" : [20],
          "title" : [21],
          "video" : [22],
          "vote_average" : [23],
          "vote_count" : [24]}
}

resultats = []
resultats2 = []

#--- Programme gérant le Filtre ---

def choixCategory():
    print("Choississez votre filtre")
    i = 0
    for str in movies_metadata:
        i += 1
        print(f"{i}.{str}")
    n = int(input("Entre un nombre n: "))
    return movies_metadata[n-1]

def ChoixFiltres(Category_1):
    i = 0
    for str in Film["movies_metadata"][Category_1]:
        i += 1
        print(f"{i}.{str}")
    m = int(input("Entre un nombre m: "))
    return Film["movies_metadata"][Category_1][m-1]

# def cycle_Filtration():
#     cycle_category()
#     cycle_filtre()

    
def cycle_category():
    Category_1 = choixCategory()
    print("Catégorie choisi :", Category_1)

    return Category_1

def cycle_filtre(Category_1):

    Filtre_1 = ChoixFiltres(Category_1)
    print("Filtre choisie :", Filtre_1)

    return Filtre_1

# --- Boucle de réitération ---
MAX_ITER = 5
iteration = 0

while iteration < MAX_ITER:
    print(f"\n--- Itération {iteration + 1} ---")

    Category = cycle_category
    resultats2.append(Category)
    Filtre = cycle_filtre(Category)
    resultats.append(Filtre)

    # Question pour continuer
    choix = input("Voulez-vous continuer ? (o/n) : ").strip().lower()
    if choix == "n":
        print("Fin du programme.")
        print(resultats)
        break
        

    iteration += 1

else:
    print("Vous avez atteint le maximum de 5 répétitions.")
    print(resultats)

# --- Affichage des résultats obtenus ---
print("\n=== Résultats obtenus ===")
for i, val in enumerate(resultats, start=1):
    print(f"{i}. {val}")



def search_by_categorie(resultat: str, nb_row: int = 0) -> pd.DataFrame:
    # On filtre d'abord
    filtered = movies[movies["genres"].str.contains(resultat, case=False, na=False)]

    filtered = filtered[["original_title"]]

    # Nombre de lignes contrôlé par nb_row
    if nb_row > 0:
        return filtered.head(nb_row)
    elif nb_row < 0:
        return filtered.tail(abs(nb_row))
    else:
        return filtered

def display_all_with_pandas():
    pd.set_option('display.max_colwidth', None)

def main():
    display_all_with_pandas()
    print(search_by_categorie(resultat, nb_row=5))
    return

resultat = resultats[0]
main() 

