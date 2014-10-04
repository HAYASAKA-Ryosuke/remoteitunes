# coding:utf-8

from flask import Flask, render_template, request
import itunescontrol

app = Flask(__name__)
itunes = itunescontrol.controlitunes()


@app.route('/itunes/')
@app.route('/itunes/<param>')
def index(param=None):
    itunesstatus = param
    soundparam = request.args.get('soundvalue')
    if itunesstatus is None:
        pass
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
    return render_template('index.html', itunesstatus=itunesstatus)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
