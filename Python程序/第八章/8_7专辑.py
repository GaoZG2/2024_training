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

print(make_album('gzg', 'album0'))
print(make_album('gzg1', 'album1'))
print(make_album('gzg2', 'album2', 3))