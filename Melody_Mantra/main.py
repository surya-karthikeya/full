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
    result = search_spotify(query)
    return jsonify(result)


def search_spotify(query):
    url = "https://spotify81.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": "431293fbd2msh685c96f428f44c6p1f147ejsn46abd96a27ca",
        "X-RapidAPI-Host": "spotify81.p.rapidapi.com"
    }
    params = {"q": query, "type": "multi", "offset": "0", "limit": "10", "numberOfTopResults": "5"}

    response = requests.get(url, headers=headers, params=params)
    results = json.loads(response.content)
    album = results.get('albums')
    if album:
        item = album.get('items')
        data = []
        for i in range(len(item)):
            user = item[i].get('data')
            data.append(user)

        artist = []
        for j in range(len(data)):
            user1 = data[j].get('artists')
            artist.append(user1)

        items1 = []
        for k in range(len(artist)):
            user2 = artist[k].get('items')
            items1.append(user2)

        profile = []
        for g in range(len(items1)):
            user3 = items1[g][0].get('profile').get('name')
            profile.append(user3)

        return profile


if __name__ == '__main__':
    app.run(debug=True, port=977)
