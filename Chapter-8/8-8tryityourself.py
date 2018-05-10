# 8-7 Album:
def make_album(band_name, band_album, tracks=0):

	"""Building a dictionary"""
	music_dictionary = {
		'band_name': band_name.title(),
		'band_album': band_album.title(),
		}
	if tracks:
		music_dictionary['tracks'] = tracks
	return music_dictionary

# preparing prompts
band_prompt = "What is one of your favorite bands? "
album_prompt = "What is your favorite album of theirs? "

# prompt to quit
print("\nType 'quit' at any time to quit.")

while True:	
	band_name = raw_input(band_prompt)
	if band_name == 'quit':
		break

	band_album = raw_input(album_prompt)
	if band_album == 'quit':
		break

	discography = make_album(band_name, band_album)
	print(discography)

print("\nThanks for responding to our survey!")