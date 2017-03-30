# coding=utf-8
from __future__ import unicode_literals

from flask import jsonify
from flask import request
from flask import Response
from flask import render_template
from flask import send_from_directory

from vote_bot import app
from vote_bot import SLASH_COMMANDS_TOKEN

from vote_bot.utils import get_sorted_votes

from vote_bot.commands import call_command
from vote_bot.commands import help


@app.route("/api")
def api():
    """Входная точка API."""
    return jsonify({"data": get_sorted_votes()})


@app.route('/static/<path:path>')
def img(path):
    """Отдает статичные файлы."""
    return send_from_directory('static', path)


@app.route('/slack/vote', methods=['GET', 'POST'])
def vote():
    """Основная функция которая выполяет команды."""
    if (
            request.form.get('token') == SLASH_COMMANDS_TOKEN and
            request.form.get('user_name') not in ['vovan', 'slackbot']):

        user = request.form.get('user_name')
        user_id = request.form.get('user_id')
        text = request.form.get('text')

        call_command(text, user, user_id) if text else help(user_id)
    return Response(), 200


@app.route("/")
def index():
    """Входная точка шаблона."""
    return render_template('index.html')
