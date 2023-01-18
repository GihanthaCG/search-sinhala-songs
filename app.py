from flask import Flask, render_template, request
from search import *
from elasticsearch_dsl import Index

app = Flask(__name__)


@app.route('/searchByTitle', methods=['GET', 'POST'])
def searchByTitle():
    if request.method == 'POST':

        query = request.form['searchTerm']
        res = search_by_title(query)
        hits = res['hits']['hits']
        time = res['took']
        num_results = res['hits']['total']['value']

        return render_template('results.html', query=query, hits=hits, num_results=num_results, time=time)

    if request.method == 'GET':
        return render_template('result.html', init='True')


@app.route('/searchBySinger', methods=['GET', 'POST'])
def searchBySinger():
    if request.method == 'POST':

        query = request.form['searchTerm']
        res = search_by_artist(query)
        hits = res['hits']['hits']
        time = res['took']
        num_results = res['hits']['total']['value']

        return render_template('results.html', query=query, hits=hits, num_results=num_results, time=time)

    if request.method == 'GET':
        return render_template('result.html', init='True')


@app.route('/searchByLyricist', methods=['GET', 'POST'])
def searchByLyricist():
    if request.method == 'POST':

        query = request.form['searchTerm']
        res = search_by_lyricist(query)
        hits = res['hits']['hits']
        time = res['took']
        num_results = res['hits']['total']['value']

        return render_template('results.html', query=query, hits=hits, num_results=num_results, time=time)

    if request.method == 'GET':
        return render_template('result.html', init='True')


@app.route('/searchByAlbum', methods=['GET', 'POST'])
def searchByAlbum():
    if request.method == 'POST':

        query = request.form['searchTerm']
        res = search_by_album(query)
        hits = res['hits']['hits']
        time = res['took']
        num_results = res['hits']['total']['value']

        return render_template('results.html', query=query, hits=hits, num_results=num_results, time=time)

    if request.method == 'GET':
        return render_template('result.html', init='True')


@app.route('/searchByYear', methods=['GET', 'POST'])
def searchByYear():
    if request.method == 'POST':

        y_min = request.form['y_min']
        y_max = request.form['y_max']
        query = "From:"+str(y_min) + " To:"+str(y_max)
        res = search_by_year(y_min, y_max)
        hits = res['hits']['hits']
        time = res['took']
        num_results = res['hits']['total']['value']

        return render_template('results.html', query=query, hits=hits, num_results=num_results, time=time)

    if request.method == 'GET':
        return render_template('result.html', init='True')


@app.route('/searchByLyrics', methods=['GET', 'POST'])
def searchByLyrics():
    if request.method == 'POST':

        query = request.form['searchTerm']
        res = search_by_lyrics(query)
        hits = res['hits']['hits']
        time = res['took']
        num_results = res['hits']['total']['value']

        return render_template('results.html', query=query, hits=hits, num_results=num_results, time=time)

    if request.method == 'GET':
        return render_template('result.html', init='True')


@app.route('/customSearch', methods=['GET', 'POST'])
def customSearch():
    if request.method == 'POST':
        # return "hellow"
        query = "hellow"
        title = request.form['title']
        singer = request.form['singer']
        lyricist = request.form['lyricist']
        album = request.form['album']
        lyrics = request.form['lyrics']
        metaphor = request.form['metaphor']

        res = custom_search(title, singer, lyricist, album, lyrics, metaphor)
        # res = custom_search("oba","roshan","","","","moon")
        hits = res['hits']['hits']
        time = res['took']
        num_results = res['hits']['total']['value']

        return render_template('results.html', query=query, hits=hits, num_results=num_results, time=time)

    if request.method == 'GET':
        return render_template('result.html', init='True')


if __name__ == '__main__':
    app.run()
