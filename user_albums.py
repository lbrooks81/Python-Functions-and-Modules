def make_album(artist : str, title : str, number_of_songs : int = None) -> dict:
    """Returns a dictionary for an album given the artist and the title"""
    # Checks if optional number of songs argument was passed
    if number_of_songs:
            album : dict = {'artist' : artist, 'title': title, 'number of songs' : number_of_songs}

    else:
        album : dict = {'artist' : artist, 'title': title}
    return album


artist : str = ''
while True:
    print("You will enter information for an album. (Or else)")
    artist = input("Please enter the artist's name or enter \'quit\' to quit: ")
    if artist.casefold() == 'quit':
         break
    title : str = input("Please enter the album's title: ")
    user_input : str = input("Please enter the number of songs on the album or leave blank if you don't know: ")
    number_of_songs : int = int(user_input) if user_input.isdigit() else None
    album : dict = make_album(artist, title, number_of_songs)
    print(album)