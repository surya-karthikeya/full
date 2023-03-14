from flask import Flask, request, render_template, jsonify
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('tune.html')


@app.route('/spotify/search')
def search():
    query = request.args.get('query')
    results = search_spotify(query)
    return jsonify(results)


def search_spotify(query):
    url = "https://spotify81.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": "431293fbd2msh685c96f428f44c6p1f147ejsn46abd96a27ca",
        "X-RapidAPI-Host": "spotify81.p.rapidapi.com"
    }
    params = {"q": query, "type": "multi", "offset": "0", "limit": "10", "numberOfTopResults": "5"}

    response = requests.get(url, headers=headers, params=params)
    results = json.loads(response.content)
    return results


if __name__ == '__main__':
    app.run(debug=True, port=9779)
