import requests

def fetch_lyrics(artist_name, song_name):
    try:     
        param = song_name + " " + artist_name
        param = param.replace(' ', '+')
        res = requests.get("https://www.jiosaavn.com/api.php?__call=autocomplete.get&_format=json&_marker=0&includeMetaTags=1&query={param}".format(param = param)).json()
        try:
            song_id=res['songs']['data'][0]['id']
            res = requests.get("https://www.jiosaavn.com/api.php?__call=lyrics.getLyrics&ctx=web6dot0&api_version=4&_format=json&_marker=0%3F_marker%3D0&lyrics_id={id}".format(id=song_id)).json()
            lyrics =  res['lyrics'].replace('<br>', "\n")
            return {"lyrics": lyrics}
        except:
            return {"Error": "Not found"}
    except Exception as e:
        return {"Error": e}    