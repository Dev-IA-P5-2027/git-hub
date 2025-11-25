import sqlite3

def connect_to_base(BDD_name):
    try:
        connexion = sqlite3.connect(BDD_name)
        print(f"Gongratulation {BDD_name}")
        return connexion
    except sqlite3.Error as e:
        print(f"Erreur de connexion : {e}")
        return None
    
def get_artist_by_id(cursor, artist_id):
    query = "SELECT * FROM artists WHERE ArtistId = ?"
    cursor.execute(query, (artist_id,))
    print("GG")
    result = cursor.fetchone()
    if result:
        columns = [column[0] for column in cursor.description]
        print("GG")
        return dict (zip(columns, result))
    else:
        return None
    
def get_artist_by_name(cursor, artist_name):
    query = "SELECT * FROM artists WHERE Name = ?"
    cursor.execute(query, (artist_name,))
    print("GG")
    result = cursor.fetchone()
    if result:
        columns = [column[0] for column in cursor.description]
        print("GG")
        return dict (zip(columns, result))
    else:
        return None
    
def get_albums_by_artist(cursor, artist_id):
    query = "SELECT * FROM albums WHERE ArtistId = ?"
    cursor.execute(query, (artist_id,))
    print("GG")
    result = cursor.fetchone()
    if result:
        columns = [column[0] for column in cursor.description]
        print("GG")
        return dict (zip(columns, result))
    else:
        return None

# def get_cible_by_id(cursor, cible):
#     query = f"SELECT * FROM {cible} WHERE id = ?"
#     cursor.execute(query, (cible))
#     result = cursor.fetchone()
#     if result:
#         columns = [column[0] for column in cursor.description]
#         return dict (zip(columns, result))
#     else:
#         return None
# connexion = connect_to_base("chinook.db")


# curseur = connexion.cursor()
# curseur.execute()
# connexion.commit()
# curseur.close()
# connexion.close()



