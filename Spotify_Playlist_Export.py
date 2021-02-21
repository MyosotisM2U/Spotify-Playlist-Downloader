import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

#Get client credentials to use the Spotipy API
def get_credentials():
    client_id = input("Enter client id: ")
    client_secret = input("Enter client secret: ")
    myCredentials = (client_id, client_secret)
    return myCredentials

#Using the client credentials for the API
myCredentials = get_credentials()
client_id = myCredentials[0]
client_secret = myCredentials[1]

auth_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
playlists = sp.user_playlists('spotify')

#Returns the playlist's id based on the given uri
def get_playlist_id(playlist_uri):
    return playlist_uri[17:]

#Accepts a playlist's id and returns its title
def get_playlist_title(playlist_id):   
    title = sp.playlist(playlist_id, fields = 'name')['name']
    return title

#Returns a list of the playlist's track_ids
def get_track_ids(playlist_id):
    offset = 0
    fields = 'items.track.id,total'
    response = sp.playlist_tracks(playlist_id, offset = offset, fields = fields, additional_types = ['track'])
    track_ids = []

    for track_d in response['items']:
        track_ids.append(track_d['track']['id'])
    
    return track_ids

#Accepts a list of track_ids and returns a list of their respective titles
def get_track_titles(track_ids):
    track_titles = []
    for track_id in track_ids:
        track_name = sp.track(track_id)['name']
        track_artists = sp.track(track_id)['artists'][0]['name']
        track_titles.append(track_artists + " " + track_name)
    return track_titles


