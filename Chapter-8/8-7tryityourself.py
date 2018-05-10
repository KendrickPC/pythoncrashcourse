# 8-7 Album:
def make_album(artist_name, artist_album_title, number_of_tracks=''):

	album_info = {'band_name': artist_name.title(), 'band_album': artist_album_title.title()}
	if number_of_tracks:
		album_info['number_of_tracks'] = number_of_tracks
	print(album_info)

make_album('coldplay', 'a head full of dreams', 12)
make_album('jp cooper', 'raised under grey skies', 20)
make_album('taylor swift', 'reputation', 15)