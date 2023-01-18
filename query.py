import json


def search_songs_by_title(query):
    q = {
        "query": {
            "match_phrase_prefix": {
                "song_title.case_insensitive_and_inflections": {
                    "query" :query,
                    "zero_terms_query": "all"}
            }
        }
    }    
    return q


def search_songs_by_artist(query):
    q = {
        "query": {
            "match_phrase_prefix": {
                "singer.case_insensitive_and_inflections": query
            }
        }
    }   
    return q


def search_songs_by_lyricist(query):
    q = {
        "query": {
            "match_phrase_prefix": {
                "lyricist.case_insensitive_and_inflections": query
            }
        }
    }   
    return q

def search_songs_by_album(query):
    q = {
        "query": {
            "match_phrase_prefix": {
                "album.case_insensitive_and_inflections": query
            }
        }
    }   
    return q


def search_songs_by_year(y_min, y_max):
    q = {
        "query": {
            "range": {
            "year": {"gte": y_min, "lte": y_max}
            }
        }
    }  
    return q


def search_songs_by_lyrics(query):
    q = {
        "query": {
            "match_phrase_prefix": {
                "song_lyrics.case_insensitive_and_inflections": query
            }
        }
    }   
    return q


def search_songs_by_metaphor(query):
    q = {
        "query": {
            "match_phrase_prefix": {
                "metaphors.meaning.case_insensitive_and_inflections": query
            }
        }
    }   
    return q


def custom_search_songs(title, singer, lyricist, album, lyrics, metaphor):
    q = {
        "query": {
            "bool": {
                "must": [
                    { 
                        "match_phrase_prefix": {
                            "song_title.case_insensitive_and_inflections":{ 
                            "query":title,
                            "zero_terms_query": "all"
                            }
                        }
                    },
                    { 
                        "match_phrase_prefix": {
                            "singer.case_insensitive_and_inflections":{ 
                            "query":singer, 
                            "zero_terms_query": "all"
                            }
                        }
                    },
                    { 
                        "match_phrase_prefix": {
                            "lyricist.case_insensitive_and_inflections":{ 
                            "query": lyricist, 
                            "zero_terms_query": "all"
                            }
                        }
                    },
                    { 
                        "match_phrase_prefix": {
                            "album.case_insensitive_and_inflections":{ 
                            "query":album, 
                            "zero_terms_query": "all"
                            }
                        }
                    },
                    { 
                        "match_phrase_prefix": {
                            "song_lyrics.case_insensitive_and_inflections":{ 
                            "query":lyrics,
                            "zero_terms_query": "all"
                            }
                        }
                    },
                    { 
                        "match_phrase_prefix": {
                            "metaphors.meaning.case_insensitive_and_inflections":{ 
                            "query": metaphor,
                            "zero_terms_query": "all"
                            }
                        }
                    }
                ]
            }
        }
    }   
    return q









