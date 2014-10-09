# coding:utf-8

from flask import Flask, render_template, request
import itunescontrol
import leveldb

app = Flask(__name__)

db = leveldb.DataBase()
itunes = itunescontrol.controlitunes()
keys, vals = db.readmusic()
music = [x['musicname'] for x in vals]
artist = [x['artistname'] for x in vals]
album = [x['albumname'] for x in vals]

@app.route('/itunes/')
@app.route('/itunes/<param>')
def index(param=None):
    itunesstatus = param
    soundparam = request.args.get('soundvalue')
    music = None
    artist = None
    album = None
    if itunesstatus is None:
        keys, vals = db.readmusic()
        music = [x['musicname'] for x in vals]
        artist = [x['artistname'] for x in vals]
        album = [x['albumname'] for x in vals]
    if soundparam is not None:
        itunes.volume(soundparam)
    if itunesstatus == 'play':
        itunes.play()
    elif itunesstatus == 'pause':
        itunes.pause()
    if itunesstatus == 'forward':
        itunes.nexttrack()
    if itunesstatus == 'backward':
        itunes.prevtrack()
    return render_template('index.html', itunesstatus=itunesstatus, musiclist=zip(music, artist, album))


if __name__ == '__main__':

    app.run(debug=False, host='0.0.0.0')
