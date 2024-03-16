from flask import Flask , render_template
import requests

#kode
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bestplayers')
def premier():
    url = "https://transfermarkt-db.p.rapidapi.com/v1/markets/best-players"

    querystring = {"locale":"DE"}

    headers = {
        "X-RapidAPI-Key": "de0d601b2cmsh8de344ce1e5998fp159ceejsn547abd8fe47b",
        "X-RapidAPI-Host": "transfermarkt-db.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    players = response.json()
    return render_template('bestplayer.html', data = players)
    

@app.route('/mvp')
def players():
    url = "https://transfermarkt-db.p.rapidapi.com/v1/markets/most-valuable-players"

    querystring = {"locale":"DE"}

    headers = {
        "X-RapidAPI-Key": "de0d601b2cmsh8de344ce1e5998fp159ceejsn547abd8fe47b",
        "X-RapidAPI-Host": "transfermarkt-db.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    mvp = response.json()
    return render_template('mvp.html', data = mvp )

#script
if __name__ == '__main__':
    app.run(debug=True) #jika ada perubahan bisa langsung diupdate)
