from flask import render_template, jsonify
from datetime import datetime
from copaticket import app
from cartolafc import *


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', year=datetime.now().year)


@app.route('/api/aliga', methods=['GET'])
def liga():
    league = get_league()
    return jsonify(league)


@app.route('/api/times', methods=['GET'])
def times():
    league = get_league()
    return jsonify(league['times'])


@app.route('/api/rodada', methods=['GET'])
def rodada():
    game = get_game()
    return jsonify(game)


@app.route('/api/time/<team_slug>', methods=['GET'])
def time(team_slug):
    team = get_team(team_slug)
    return jsonify(team)
