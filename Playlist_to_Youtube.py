from youtube_search import YoutubeSearch
import Spotify_Playlist_Export as export

track_ids = export.get_track_ids('spotify:playlist:6NlfAHFTrL0MCdj7CEJ7el')
track_titles = export.get_track_titles(track_ids)
test_list = track_titles

#Returns the given song's url
#Add a try and except block for section list renderer error
def get_url(song_title):
    try:
        results = YoutubeSearch(song_title, max_results = 10).to_dict()
        if len(results) > 0:    
            url = "youtube.com" + results[0]['url_suffix']
            return url
        print("Error: No results found")
        return "N\\A"
    except: 
        return "N\\A"

#Accepts a list of track titles and returns a list of their respective urls
def get_urls(track_titles):
    url_list = []
    for song_title in track_titles:
        url = get_url(song_title)
        if url != "N\\A":
            url_list.append(url)
    return url_list
