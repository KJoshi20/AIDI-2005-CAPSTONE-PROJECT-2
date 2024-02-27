from flask import Flask, render_template, request, jsonify
from datetime import datetime
from ytmusicapi import YTMusic
import json

from urllib.request import urlopen
from io import BytesIO

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///luna.db'
app.config['SQLALCHEMY_ECHO'] = True



# Routing
@app.route('/', methods=['GET'])
def homepage():
    ytmusic = YTMusic()
    home_data = ytmusic.get_home(10)
    artists = []
    #genre = ytmusic.get_mood_categories()

    default_songs = []

    for data in home_data:
        if data['title'] == 'Recommended playlists':
            recommended_playlists = data['contents']
            print("RECOMMENDED")
            print("-----------")
            print("")
        elif data['title'] == 'Quick picks':
            default_songs = data['contents']
            index=0;
            while artists==[]:
                try:
                    artists = ytmusic.get_artist(default_songs[index]["artists"][0]["id"])[
                    'related']['results']
                    json_object = json.dumps(artists, indent=4)
                    f = open("trial.txt", 'w')
                    f.write(json_object)
                except:
                    index+=1
    print(default_songs)
    return render_template('index.html', default_songs=default_songs)

