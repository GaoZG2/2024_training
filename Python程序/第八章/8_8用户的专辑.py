def make_album(singer, album_name, songs=None):
    if songs:
        album_info = {
            'singer': singer,
            'album': album_name,
            'songs': songs
        }
    else:
        album_info = {
            'singer': singer,
            'album': album_name
        }
    return album_info

while True:
    artist = input("Enter the singer's name (or 'quit' to finish): ")
    if artist.lower() == "quit":
        break
    album_name = input("Enter the album's name: ")
    songs = input("Enter the number of songs of the album: ")
    songs = int(songs)
    if songs == 1:
        songs = None
    info = make_album(artist, album_name, songs)
    print(info)