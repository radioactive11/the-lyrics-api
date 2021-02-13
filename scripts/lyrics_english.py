from bs4 import BeautifulSoup
import requests
import re

def fetch_lyrics(artist_name, song_name):
    try:
        song_name = re.sub('[\W_]+', '', song_name).lower()
        artist_name = re.sub('[\W_]+', '', artist_name).lower()
        url = "https://www.azlyrics.com/lyrics/{aname}/{sname}.html".format(aname=artist_name, sname=song_name)
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'lxml')
        divs = soup.find_all("div", {"class": ""})
        try:
            lyrics = divs[1].text
            lyrics = lyrics[2: -1]
            return {"lyrics": lyrics}
        except Exception as e:
            print(e)
            return {"Error": "Not found"}
        
    except Exception as e:
        print(e)
        return {"Error": e}