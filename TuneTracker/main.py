from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        url = "https://spotify81.p.rapidapi.com/search"

        querystring = {"q": query, "type": "multi", "offset": "0", "limit": "10", "numberOfTopResults": "5"}

        headers = {
            "X-RapidAPI-Key": "431293fbd2msh685c96f428f44c6p1f147ejsn46abd96a27ca",
            "X-RapidAPI-Host": "spotify81.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        return render_template('tune.html', data=data)
    else:
        return render_template('tune.html')


if __name__ == '__main__':
    app.run(debug=True)
