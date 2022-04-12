from argparse import Namespace
from base64 import encode
from lyricli import melon
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False

@app.route("/lyrics/<title>", methods=['GET'])
@app.route("/lyrics/<title>:<artist>", methods=['GET'])
def get_lyrics(title: str=None, artist: str=None):
    form = Namespace(title=title, artist=artist, debug=False)
    lyrics = melon.get_lyrics(form)
    print(lyrics)
    return jsonify(list(lyrics))
