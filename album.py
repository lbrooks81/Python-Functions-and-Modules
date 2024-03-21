def make_album(artist : str, title : str, number_of_songs : int = None) -> dict:
    """Returns a dictionary for an album given the artist and the title"""
    if number_of_songs:
            album : dict = {'artist' : artist, 'title': title, 'number of songs' : number_of_songs}
    else:
        album : dict = {'artist' : artist, 'title': title}
    return album

best_album = make_album('Yes', 'Close to the Edge', 3)
print(best_album)

coolest_album = make_album('Metallica', 'Master of Puppets')
print(coolest_album)

chillest_album = make_album('Pink Floyd', 'The Dark Side of the Moon')
print(chillest_album)