from flask import Flask, render_template, request, jsonify
import requests
import logging

app = Flask(__name__, template_folder="templates")
logging.basicConfig(filename='app.log', level=logging.DEBUG)


@app.route("/")
def index():
    return render_template('tune.html')


@app.route('/spotify/search')
def home():
    try:
        query = request.args.get('query')
        url = "https://spotify81.p.rapidapi.com/search"

        querystring = {"q": query, "type": "multi", "offset": "0", "limit": "10", "numberOfTopResults": "5"}

        headers = {
            "X-RapidAPI-Key": "431293fbd2msh685c96f428f44c6p1f147ejsn46abd96a27ca",
            "X-RapidAPI-Host": "spotify81.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)

    except requests.exceptions.HTTPError as err:
        logging.error(f'HTTP error occurred: {err}')
        return jsonify({'error': str(err)})


if __name__ == '__main__':
    app.run(debug=True)
