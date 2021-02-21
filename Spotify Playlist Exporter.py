import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

def get_credentials():
    print("Enter client id: ")
    client_id = input()
    print("Enter client secret ")
    client_secret = input()
    myCredentials = (client_id, client_secret)
    return myCredentials

myCredentials = get_credentials()
client_id = myCredentials[0]
client_secret = myCredentials[1]

auth_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists('spotify')

playlist_uri = 'spotify:playlist:37i9dQZF1DWT7XSlwvR1ar'
playlist_id = playlist_uri[17:]
print(playlist_id)
offset = 0
fields = 'items.track.id,total'



response = sp.playlist_tracks(playlist_id, offset = offset, fields = fields, additional_types = ['track'])
pprint(response['items'])
offset = offset + len(response['items'])
print(offset, "/", response['total'])

track_ids = []
for track_d in response['items']:
    track_ids.append(track_d['track']['id'])
pprint(track_ids)

tracks = []
for track_id in track_ids:
    track_name = sp.track(track_id)['name']
    #print(track_name)
    tracks.append(track_name)
    #tracks.append([track['name']])
pprint(tracks)

#track_id = '4hrJhMznNddR7UThDKHSJy'
#track = sp.track(track_id)
#pprint(track['name'])