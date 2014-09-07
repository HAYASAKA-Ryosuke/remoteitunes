# coding:utf-8

from flask import Flask, render_template, request

app = Flask(__name__)

def playmusic():
    pass

def pausemusic():
    pass

@app.route('/itunes/')
@app.route('/itunes/<param>')
def index(param=None):
    itunesstatus = param
    print(request.args.get('soundvalue'))
    if itunesstatus == 'play':
        playmusic()
    else:
        pausemusic()
    return render_template('index.html', itunesstatus=itunesstatus)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
