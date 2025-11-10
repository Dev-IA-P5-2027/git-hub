import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print(pd.__version__)

movies_metadata = pd.read_csv(r"C:\Users\jesse.richard\Desktop\Mes projets\Projet Python\movies_metadata.csv", sep = ",")
credits = pd.read_csv(r"C:\Users\jesse.richard\Desktop\Mes projets\Projet Python\credits.csv", sep = ",")

#"""" print(movies_metadata["belongs_to_collection"])

movies_metadata = ["adult", "belongs_to_collection", "budget","genres", "homepage", "id", "imdb_id", "original_language", "original_title", "overview",
"popularity", "poster_path", "production_companies", "production_countries", "release_date", "revenue", "runtime", "spoken_languages", "status", "tagline",
"title", "video", "vote_average", "vote_count"]


Film = {"movies_metadata" : 
          {"adult": [True, False],
          "belongs_to_collection" : [2],
          "budget" : [30000000, 65000000, 16000000],
          "genres" : ["Animation", "Adventure", "Romance", "Comedy", "Drama", "Action"],
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

def ChoixFiltres2():
    print("Choississez votre filtre")
    i = 0
    for str in movies_metadata:
        i += 1
        print(f"{i}.{str}")
    n = int(input("Entre un nombre n: "))
    return movies_metadata[n-1]

def ChoixFiltres3(Filtre_1):
    i = 0
    for str in Film["movies_metadata"][Filtre_1]:
        i += 1
        print(f"{i}.{str}")
    m = int(input("Entre un nombre m: "))
    return Film["movies_metadata"][Filtre_1][m-1]


Filtre_1 = ChoixFiltres2()
print(Filtre_1)
Filtre_2 = ChoixFiltres3(Filtre_1)
print(Filtre_2)
# valeur = ChoixFiltres()
    
# # Filtre_1 = Filtration()
# # Filtre_2 = Filtration()
# # Filtre_3 = Filtration()
# # Filtre_4 = Filtration()
# # Filtre_5 = Filtration()

# print(f"Vos filtre : {Filtre_1}, {Filtre_2}, {Filtre_3}, {Filtre_4}, {Filtre_5}")
# # print("Salut")

# #Film = {"Film : Genre : [Liste des genre dans le csv]"}
# #revoir le truc de brillant

