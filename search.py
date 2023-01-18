from elasticsearch import Elasticsearch

from query import *


INDEX = 'sinhala-song-lyrics'
client = Elasticsearch(HOST="http://localhost", PORT=9200)


def search_by_title(query):
    query_body = search_songs_by_title(query)
    print('Searching songs by title')
    res = client.search(index=INDEX, body=query_body)
    return res


def search_by_artist(query):
    query_body = search_songs_by_artist(query)
    print('Searching songs by artist')
    res = client.search(index=INDEX, body=query_body)
    return res


def search_by_lyricist(query):
    query_body = search_songs_by_lyricist(query)
    print('Searching songs by lyricist')
    res = client.search(index=INDEX, body=query_body)
    return res


def search_by_album(query):
    query_body = search_songs_by_album(query)
    print('Searching songs by album')
    res = client.search(index=INDEX, body=query_body)
    return res


def search_by_year(query_1, query_2):
    query_body = search_songs_by_year(query_1, query_2)
    print('Searching songs by album')
    res = client.search(index=INDEX, body=query_body)
    return res


def search_by_lyrics(query):
    query_body = search_songs_by_lyrics(query)
    print('Searching songs by lyrics')
    res = client.search(index=INDEX, body=query_body)
    return res


def custom_search(title, singer, lyricist, album, lyrics, metaphor):
    query_body = custom_search_songs(
        title, singer, lyricist, album, lyrics, metaphor)
    print('Searching songs by lyrics')
    res = client.search(index=INDEX, body=query_body)
    return res
