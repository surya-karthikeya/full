from flask import Flask, request, render_template, jsonify
import requests
import json
from flask_cors import CORS

app = Flask(__name__)
origins = ['http://localhost:3000']
CORS(app, origins=origins)


@app.route('/movie/search')
def search():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    res = search_movie(query, page)
    result = {'success': True, 'data': res}
    return jsonify(result)


def search_movie(query, page):
    url = f"https://moviesdatabase.p.rapidapi.com/titles/search/keyword/{query}"
    querystring = {"page":f"{page}","limit":"3"}

    headers = {
	    "X-RapidAPI-Key": "431293fbd2msh685c96f428f44c6p1f147ejsn46abd96a27ca",
	    "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    results = json.loads(response.content)
    results = results.get('results', {})
    try:
        if results:
            id = []
            for element in results:
                id.append(element.get('id', []))

            primary = []
            for i in results:
                primary.append(i.get('primaryImage', []))

            url = []
            for j in primary:
                url.append(j.get('url', []))

            result = []
            for item1, item2 in zip(id, url):
                result.append({'id': item1, "image": item2})

            return result
        else:
            return {'error': f'Missing required key'}
    except KeyError as e:
        return {'error': f'Missing required key{e}'}



if __name__ == '__main__':
    app.run(debug=True)
