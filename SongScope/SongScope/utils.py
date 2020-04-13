import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



def playlist_tracker(artist):
    # initialize credentials, and categories
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    response = sp.search(q=artist, limit=20, offset=0, type='track', market='US')
    songs = response
    print(response)

    return songs


def track_data(track_id):
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    audio_features = sp.audio_features(track_id)[0]

    # Get Key
    pitch = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    key_pitch = pitch[audio_features['key']]
    if audio_features['mode']:
        key = f"{key_pitch} Major"
    else:
        key = f"{key_pitch} Minor"
    audio_features['key'] = key

    # Get Track Length
    time = msConversion(audio_features['duration_ms'])
    audio_features['time'] = time
    audio_features['popularity'] = sp.track(track_id)['popularity']
    audio_features['preview_url'] = sp.track(track_id)['preview_url']
    audio_makeup = [
        audio_features['acousticness'],
        audio_features['danceability'],
        audio_features['energy'],
        audio_features['instrumentalness'],
        audio_features['liveness'],
        audio_features['speechiness']
    ]
    print(audio_makeup)

    audio_features['makeup'] = audio_makeup

    return audio_features


def album_data(album_id):
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    album_features = sp.album(album_id)
    album_payload = {
        'image': album_features['images'][0]['url'],
        'copyrights': album_features['copyrights'][0]['text'],
        'label': album_features['label'],
        'popularity': album_features['popularity'],
        'release_date': album_features['release_date'],
        'name': album_features['name']
    }

    return album_payload


def msConversion(ms):
    millis = int(ms)
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = (millis / (1000 * 60 * 60)) % 24

    return "%d:%d" % (minutes, seconds)


def load_data(queryset, artist):
    payload = []
    for i in range(20):
        payload.append({'image': queryset['tracks']['items'][i]['album']['images'][2]['url'],
                        'artist': queryset['tracks']['items'][i]['artists'][0]['name'],
                        'song': queryset['tracks']['items'][i]['name'],
                        'songId': queryset['tracks']['items'][i]['id'],
                        'albumId': queryset['tracks']['items'][i]['album']['id'],
                        'userInput': artist})
    return payload