from Chinook import connect_to_base
from Chinook import get_artist_by_id
from Chinook import get_artist_by_name
from Chinook import get_albums_by_artist

connexion = connect_to_base("chinook.db")
curseur = connexion.cursor()

#===Requêtes d'extraction===
artiste_id = get_artist_by_id(curseur, artist_id=1)
artiste_name = get_artist_by_name(curseur, "AC/DC" )
album_id = get_albums_by_artist(curseur, 1)
print(artiste_id)
print(artiste_name)
print(album_id)