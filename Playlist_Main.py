from pytube import YouTube
from pytube import Playlist
import pytube
from youtube_search import YoutubeSearch
import Playlist_to_Youtube as pl_list
import Spotify_Playlist_Export as export

def main():
    playlist_uri = input("Enter the uri of the playlist you want to download: ")
    print("Compiling Tracks into a list...")
    playlist_id = export.get_playlist_id(playlist_uri)
    playlist_title = export.get_playlist_title(playlist_id)
    track_ids = export.get_track_ids(playlist_id)
    track_titles = export.get_track_titles(track_ids)
    track_urls = pl_list.get_urls(track_titles)
    print("Creating a directory for the playlist...")
    abs_path = get_path(playlist_title)
    download_playlist(abs_path, track_titles, track_urls, playlist_title)



#Asks for the playlist link
#link = input("Enter the link of YouTube playlist you want to download:  ")
#p = Playlist(link)
#yt = YouTube(link)

#Returns absolute path of the playlist directory
def get_path(playlist_title):
    rel_path = "Playlists\\" + playlist_title
    abs_path = pytube.helpers.target_directory(rel_path)
    print(abs_path)
    return abs_path

#Downloads the playlist's songs and stores it in a new directory

#def download_playlist(abs_path):
    #print(f'Downloading Playlist: {p.title}')
    #for video in p.videos:
       #print(f'Downloading mp4: {video.title}')
        #video.streams.get_audio_only().download(abs_path)
    #print("Done!")

def download_playlist(abs_path, track_titles, track_urls, playlist_title):
    print(f'Downloading Playlist: {playlist_title}')
    track_count = 0
    for url in track_urls:
        print(f'Downloading: {track_titles[track_count]}')
        video = YouTube(url)
        video.streams.get_audio_only().download(abs_path)
        track_count += 1
    print("Done!")

if __name__ == "__main__":
    main()


        





