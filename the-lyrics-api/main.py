from fastapi import FastAPI
from pydantic import BaseModel
import re
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import json
from scripts import lyrics_english, lyrics_hindi

app = FastAPI()

class QueryModel(BaseModel):
    artist: str
    song: str
    lang: Optional[str] = 'eng'
    
    
app = FastAPI()


@app.get('/lyrics')
async def get_lyrics(query: QueryModel):
    artist_name = query.artist
    song_name = query.song
    
    if query.lang == 'eng':
        lyrics =  lyrics_english.fetch_lyrics(artist_name, song_name)
        return lyrics
    
    elif query.lang == 'hin':
        return lyrics_hindi.fetch_lyrics(artist_name, song_name)
    
    else:
        return {"Error": "undefined value in lang"}
