from flask import Flask, url_for, request, render_template, redirect
from jinja2 import Markup
from soundcloudRanker import *
from entryManager import entryManager

#stylePage = url_for('static', filename='style.css')
app = Flask(__name__)
app.jinja_env.globals.update(getHighestCount=getHighestCount)
app.jinja_env.globals['include_raw'] = lambda filename : Markup(app.jinja_loader.get_source(app.jinja_env, filename)[0])



@app.route('/')
def mainPage(entries=None):
    return render_template('main.html', entries= entryManager.getEntries())

@app.route('/songs/')
def songsPage(entries=None):
    return render_template('songs.html', entries= entryManager.getEntries())


@app.route('/songs/<songid>')
def song(songid=None):
    return render_template('song.html', entry=entryManager.getEntry(songid))


@app.route('/actions', methods=['GET'])
def actions():
    if request.method == 'GET':
        if (request.args.get('action') == 'update'):
            entryManager.update()
        if (request.args.get('action') == 'delete'):
           entryManager.removeFiles() 
        if (request.args.get('action') == 'rate'):
           entryManager.rateEntries()
           print("WORKED")
        else:
            error = 'No actions'
    return redirect(request.referrer)

@app.route('/display', methods=['GET'])
def display():
    if request.method == 'GET':
        if (request.args.get('file') == 'entries'):
            return render_template('display.html', filename='entries.txt')
        if (request.args.get('file') == 'ids'):
            return render_template('display.html', filename='ids.txt')
        if (request.args.get('file') == 'logs'):
            return render_template('display.html', filename='messages.log')
    return render_template('display.html')


if __name__ == '__main__':
    entryManager = entryManager()
    app.run(host='0.0.0.0', debug=True)

