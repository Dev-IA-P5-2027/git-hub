Nom_du_Programme = "Genérateur de CV"

Nom = "Richard"
Prénom = "Jesse"
Photo = "" # adresse de la photo sur ordinateur ou fichier
Titre = input("Entre le titre du travaille où tu postule")
Citation = 'Il faut être entousiaste de son métier pour y exceller' + "Denis Diderot"
Expérience = ["CDD encadrant SNU(2022)", "Stage 3° : asisatnt en pharmacie"]
Compétence = ["calme", "concrétissant ses idées", "acquis des compétence d'apprentissage au cours de mon cursus"]
Compétence2 = {
"SavoirEtre" : {"En équipe" : ["Chef d'équipe capacité à manager", "esprit d'équipe", "Inteligence émotionnel", "Adaptation du language"]}, 
"SavoirFaire" : {"En programmation" : ["Compréhension et résonnement algorythmique"]}
} 
Formation = ["Dévelopeur concepteur en IA", "Licence de Géologie de 2020 à 2025 jusqu'en L2", "BAC obtenue en 2016", "BIA obtenur en 2016"]
#Diver = {{"Hobby" : "Programmation jeux vidéo"}, {"Permis" : "en cours"}}
Benevolat = ["Bénévole associatif (JAL)", "Bénévole accompagnateur centre de loisirs et scolaire", "Scrutateur électoral"]
Numéro_de_téléphone = "06 48 14 58 46"
Adresse_Mail = "jessesteven26@gmail.com"
Language_de_Programmation = ["Python", "XML","LUA", "FLA"]
Extention = ["SWF"]
Logiciel = ["Microsoft Visual Studio", "CHAT GPT", "GIMP", "Suite Office"]



def CV():
    print(f"{Nom} {Prénom}")

    print("Organisme ciblé : ")
    print(Titre)

    print("Citation :")
    print(Citation)

    print("Compétence :")
    print(Compétence)
    print(Compétence2["SavoirEtre"]["En équipe"][0])

    print("Language de Prgrammation maîtrisé :")
    print(Language_de_Programmation)

    print("Extention maîtrisé :")
    print(Extention)

    print("Logiciel maîtrisé :")
    print(Logiciel)

    print("Formations")
    print(Formation)

    print("Expérience :")
    print(Expérience)

    # print("Divers :")
    # print(Diver["Hobby"][1])

    print("Bénévolat :")
    print(Benevolat)

    print("Adresse mail :")
    print(Adresse_Mail)

    print("Numéro de Téléphone :")
    print(Numéro_de_téléphone)

CV()
