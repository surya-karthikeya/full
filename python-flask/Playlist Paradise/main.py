from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__, template_folder="templates")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        find = request.form.get("country")

        url = "https://spotify81.p.rapidapi.com/top_200_tracks"

        querystring = {"country": find}

        headers = {
            "X-RapidAPI-Key": "431293fbd2msh685c96f428f44c6p1f147ejsn46abd96a27ca",
            "X-RapidAPI-Host": "spotify81.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        find = json.loads(response.text)
        return render_template("find.html", find=find)
    else:
        return render_template('find.html')


if __name__ == '__main__':
    app.run(debug=True)
