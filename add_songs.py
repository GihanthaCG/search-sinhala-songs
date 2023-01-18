from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json, re
import codecs
import unicodedata

client = Elasticsearch(HOST="http://localhost", PORT=9200)
INDEX = 'search-sinhala-songs'

def createIndex():
    index = Index(INDEX, using=client)
    res = index.create()
    print(res)

def read_all_songs():
    with open('songs/songs.json', 'r', encoding='utf-8-sig') as f:
        all_songs = json.loads("[" +
                          f.read().replace("}\n{", "},\n{") +"]")
        res_list = [i for n, i in enumerate(all_songs) if i not in all_songs[n + 1:]]
        return res_list

def addSongs(song_array):
    for song in song_array:
        # Fields-capturing
        # print(song)
        song_title = song.get("song_title", None)
        song_lyrics = song.get("song_lyrics",None)
        lyricist = song.get("lyricist",None)
        singer = song.get("singer",None)
        album = song.get("album",None)
        year = song.get("year",None)
        metaphors = song.get("metaphors",None)


        yield {
            "_index": "tamilsonglyrics",
            "_source": {
                "song_title": song_title,
                "song_lyrics": song_lyrics,
                "lyricist": lyricist,
                "singer": singer,
                "album": album,
                "year": year,
                "metaphors": metaphors
            },
        }


# createIndex()
all_songs = read_all_songs()
helpers.bulk(client,addSongs(all_songs))