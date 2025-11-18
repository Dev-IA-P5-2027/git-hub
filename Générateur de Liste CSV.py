def list_langues() -> list:
    # Lecture du fichier
    # movies = pd.read_csv(r"C:\Users\Jayso\Desktop\GitHub\Projet python\data\movies_metadata.csv", sep = ",", low_memory=False)
    movies = pd.read_csv(r"C:\Users\jesse.richard\Desktop\Mes projets\Projet Python\data\movies_metadata.csv", sep = ",", low_memory=False)

    langues_set = set()

    for entry in movies["langues"].dropna():
        try:
            # Convertit la chaîne JSON-like en objet Python
            langues_list = ast.literal_eval(entry)

            # Ajoute chaque genre dans l'ensemble
            for g in langues_list:
                langues_set.add(g["name"])
        except:
            pass  # ignore les lignes mal formatées

    return sorted(langues_set)

def list_pays() -> list:
    # Lecture du fichier
    # movies = pd.read_csv(r"C:\Users\Jayso\Desktop\GitHub\Projet python\data\movies_metadata.csv", sep = ",", low_memory=False)
    movies = pd.read_csv(r"C:\Users\jesse.richard\Desktop\Mes projets\Projet Python\data\movies_metadata.csv", sep = ",", low_memory=False)

    pays_set = set()

    for entry in movies["pays"].dropna():
        try:
            # Convertit la chaîne JSON-like en objet Python
            pays_list = ast.literal_eval(entry)

            # Ajoute chaque genre dans l'ensemble
            for g in pays_list:
                pays_set.add(g["name"])
        except:
            pass  # ignore les lignes mal formatées

    return sorted(pays_set)

Liste_des_pays = list_pays()
print(Liste_des_pays)

def list_production_companies() -> list:
    # Lecture du fichier
    # movies = pd.read_csv(r"C:\Users\Jayso\Desktop\GitHub\Projet python\data\movies_metadata.csv", sep = ",", low_memory=False)
    movies = pd.read_csv(r"C:\Users\jesse.richard\Desktop\Mes projets\Projet Python\data\movies_metadata.csv", sep = ",", low_memory=False)

    production_companies_set = set()

    for entry in movies["production_companies"].dropna():
        try:
            # Convertit la chaîne JSON-like en objet Python
            production_companies_list = ast.literal_eval(entry)

            # Ajoute chaque genre dans l'ensemble
            for g in production_companies_list:
                production_companies_set.add(g["name"])
        except:
            pass  # ignore les lignes mal formatées

    return sorted(production_companies_set)

Liste_des_production_companies = list_production_companies()
print(Liste_des_production_companies)

# def list_overview() -> list:
#     # Lecture du fichier
#     # movies = pd.read_csv(r"C:\Users\Jayso\Desktop\GitHub\Projet python\data\movies_metadata.csv", sep = ",", low_memory=False)
#     movies = pd.read_csv(r"C:\Users\jesse.richard\Desktop\Mes projets\Projet Python\data\movies_metadata.csv", sep = ",", low_memory=False)

#     overview_set = set()

#     for entry in movies["overview"].dropna():
#         try:
#             # Convertit la chaîne JSON-like en objet Python
#             overview_list = ast.literal_eval(entry)

#             # Ajoute chaque genre dans l'ensemble
#             for g in overview_list:
#                 overview_set.add(g["name"])
#         except:
#             pass  # ignore les lignes mal formatées

#     return sorted(overview_set)

# Liste_des_overview = list_overview()
# print(Liste_des_overview)

def list_runtime() -> list:
    # Lecture du fichier
    # movies = pd.read_csv(r"C:\Users\Jayso\Desktop\GitHub\Projet python\data\movies_metadata.csv", sep = ",", low_memory=False)
    movies = pd.read_csv(r"C:\Users\jesse.richard\Desktop\Mes projets\Projet Python\data\movies_metadata.csv", sep = ",", low_memory=False)

    runtime_set = set()

    for entry in movies["runtime"].dropna():
        try:
            # Convertit la chaîne JSON-like en objet Python
            runtime_list = ast.literal_eval(entry)

            # Ajoute chaque genre dans l'ensemble
            for g in runtime_list:
                runtime_set.add(g["name"])
        except:
            pass  # ignore les lignes mal formatées

    return sorted(runtime_set)

Liste_des_runtime = list_runtime()
print(Liste_des_runtime)