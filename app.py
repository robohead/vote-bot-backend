# coding: utf-8
import re
import os

from flask_cors import CORS
from flask import Flask, request, Response, jsonify, send_from_directory, render_template
from slackclient import SlackClient
from tinydb import TinyDB, Query

# Your server settings
DOMAIN = os.environ.get('DOMAIN')

# Slack
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
SLASH_COMMANDS_TOKEN = os.environ.get('SLASH_COMMANDS_TOKEN')

# Bot default settings
BOT_USERNAME = "Scorpion"
BOT_ICON = u"%s/static/bot.gif" % DOMAIN
DEFAULT_KWARGS = {
    # "token": SLASH_COMMANDS_TOKEN,
    "username": BOT_USERNAME,
    "icon_url": "http://www.jogosonlinepc.com.br/imagens_posts/fotoscorpion.jpg",
    "response_type": "ephemeral",
}

# Channel with members
DEFAULT_CHANNEL = os.environ.get('DEFAULT_CHANNEL')

# Flask
app = Flask(__name__, static_url_path='')
CORS(app)
slack_client = SlackClient(SLACK_TOKEN)

# Database
db = TinyDB('db.json')
Vote = Query()


def get_sorted_votes(index=None):
    u"""Возвращет отсортированный по райтингу результат."""
    return sorted(db.all(), key=lambda x: x['rank'], reverse=True)[:index]


def get_vote_as_attachment(user, vote_id, vote_content, vote_rank, voters):
    u"""Возвращает отформатированный объект предложения."""
    return {
        "author_name": u"Автор: @%s" % user,
        "title": u"#%d %s" % (vote_id, vote_content),
        "color": "good",
        "footer": u"Ранк: %d\nПроголосовавшие: %s" % (vote_rank, ', '.join(voters))
    }


def get_members(channel_id):
    u"""Получает список пользователей из канала."""
    data = slack_client.api_call(
        "channels.info",
        token=SLASH_COMMANDS_TOKEN,
        channel=channel_id
    )
    if data.get('channel'):
        return data['channel'].get('members')


def send_404(user_id, text):
    u"""Отправляет сообщение об ошибке."""
    direct_msg(user_id, None, [{"text": text, "color": "danger"}])


def direct_msg(user_id, text=None, attachments=None):
    u"""Отправляет сообщение в канал slackbot."""
    kwargs = DEFAULT_KWARGS
    kwargs['channel'] = user_id
    if text:
        kwargs['text'] = text
    if attachments:
        kwargs['attachments'] = attachments
    slack_client.api_call("chat.postMessage", **kwargs)


def add_vote(user_id, user, text):
    u"""
    Добавляет предложение в базу и отправляет сообщение в слак.

    команда: /vote add [text]
    """
    # TODO: Нужно отправлять сообщение списку пользователей
    vote = db.insert({
        'author_name': user,
        'author_id': user_id,
        'content': text,
        'rank': 0,
        'voters': []
    })
    members = get_members(DEFAULT_CHANNEL)
    attachments = [
        {
            "title": u'#%d %s' % (vote, text),
            "author_name": u'Автор: @' + user,
            "color": "good",
            "footer": u"Проголосуй c помощью команды /vote rate [id] [1-5]"
        }, {
            "title": u"Список всех предложений", "title_link": DOMAIN
        }
    ]
    if members:
        for user in members:
            direct_msg(user, u"Появилось новое предложение", attachments)


def show_vote(user_id, vote_id):
    u"""
    Показывает подробную информацию о предложении.

    команда: /vote show [id]
    """
    vote = db.get(eid=vote_id)
    if vote:
        attachments = [
            get_vote_as_attachment(
                vote['author_name'], vote.eid, vote['content'],
                vote['rank'], vote.get('voters', '-'))
        ]
        direct_msg(user_id, u"Появилось новое предложение", attachments)
    else:
        send_404(user_id, u"Сколько не проси, найти не могу.")


def rate_vote(user_id, user, vote_id, rank):
    u"""
    Проголосовать за предложение.

    команда: /vote rate [id] [1-5]
    """
    if rank in range(1, 6):
        vote = db.get(eid=vote_id)
        if vote:
            voters = vote['voters']
            if user in voters:
                # Пользователь уже голосовал за предложение
                send_404(user_id, "https://ru.wikipedia.org/wiki/%D0%90%D0%BC%D0%BD%D0%B5%D0%B7%D0%B8%D1%8F")
            else:
                rank = vote['rank'] + rank
                voters = voters + [user]
                db.update({"rank": rank, "voters": voters}, eids=[vote_id])
                attachments = [
                    get_vote_as_attachment(user, vote.eid, vote['content'], rank, voters)
                ]
                direct_msg(user_id, u"Голос принят", attachments)
        else:
            send_404(user_id, u"Ты уверен что твое сознание безгранично и есть бытие?")
    else:
        send_404(user_id, u"А-та-та, проголосовать можно только значением от 1-го до 5-ти.")


def update_vote(user_id, vote_id, text):
    u"""
    Обновляет текст предложения.

    Такая возможность должна быть только у автора предложения.

    команда: /vote update [id] [text]
    """
    vote = db.get(eid=vote_id)
    if vote:
        if user_id == vote['author_id']:
            db.update({'content': text}, eids=[vote.eid])
            attachments = [{"title": u"#%d %s" % (vote.eid, text), "color": "good"}]
            direct_msg(user_id, u"Предложение обновлено", attachments)
        else:
            send_404(user_id, u"А-та-та обновлять чужие предложения")
    else:
        send_404(user_id, u"Я пьян и не могу найти предложение с таким номером")


def delete_vote(user_id, vote_id):
    u"""
    Удаляет предложение.

    Такая возможность должна быть только у автора предложения.

    команда: /vote delete [id]
    """
    vote = db.get(eid=vote_id)
    if vote and user_id == vote['author_id']:
        db.remove(eids=[vote_id])
        attachments = [{"color": "good", "title": "#%d %s" % (vote.eid, vote['content'])}]
        direct_msg(user_id, u"Предложение удалено", attachments)
    else:
        send_404(user_id, u"Не могу удалить то, чего нет")


def list_votes(user_id):
    u"""
    Выводит список предложений начиная с самого высокого ранга.

    команда: /vote list
    """
    # Берем первые десять
    votes = get_sorted_votes(10)
    attachments = []
    for vote in votes:
        attachments.append(
            get_vote_as_attachment(
                vote['author_name'], vote.eid, vote['content'],
                vote['rank'], vote.get('voters', '-'))
        )
    direct_msg(user_id, u"Список предложений:", attachments)


def help(user_id):
    u"""
    Выводит список команд и полезную информацию о команде

    команда: /vote, /vote help
    """
    text = u"""
Список команд:

*/vote, /vote help*         - помощь по использованию команды
*/vote list*                - список всех голосований
*/vote show [id]*           - показать детали голосования
*/vote add [text]*          - добавить новое голосование
*/vote delete [id]*         - удалить голосование
*/vote rate [id] [15]*      - проголосовать за предложение
*/vote update [id] [text]*  - показать детали голосования
    """
    direct_msg(user_id, text)


@app.route('/static/<path:path>')
def img(path):
    u"""Отдает статичные файлы."""
    return send_from_directory('static', path)


@app.route('/dist/<path:path>')
def webpack(path):
    u"""Отдает статичные файлы."""
    return send_from_directory('dist', path)


@app.route('/slack/vote', methods=['GET', 'POST'])
def vote():
    u"""Основная функция которая парсит команды."""
    if (request.form.get('token') == SLASH_COMMANDS_TOKEN and
        (request.form.get('user_name') not in ['vovan', 'slackbot'])):
        # --- data ---
        user = request.form.get('user_name')
        user_id = request.form.get('user_id')
        text = request.form.get('text')
        # --- data ---
        if text:
            if text.startswith('add'):
                # /vote add [text]
                text = text.replace("add", "").strip()
                if text:
                    add_vote(user_id, user, text)
                else:
                    send_404(user_id, u"Это шутка?")
            elif text.startswith('show'):
                # /vote show [id]
                vote_id = re.search(r'(\d{1,})', text)
                if vote_id and vote_id.group():
                    show_vote(user_id, int(vote_id.group()))
                else:
                    send_404(user_id, u":sweat: Ты старался")
            elif text.startswith('list'):
                # /vote list
                list_votes(user_id)
            elif text.startswith('update'):
                # /vote update [id] [text]
                vote_id = re.findall(r'update\s(\d{1,})\s(.*)', text)
                if vote_id:
                    update_vote(user_id, int(vote_id[0]), vote_id[1])
                else:
                    send_404(user_id, u"Дима, ты пьян, иди домой")
            elif text.startswith('delete'):
                # /vote delete [id]
                vote_id = re.search(r'(\d{1,})', text)
                if vote_id and vote_id.group():
                    delete_vote(user_id, int(vote_id.group()))
                else:
                    send_404(user_id, u"Не могу удалить то, чего нет")
            elif text.startswith('help'):
                # /vote, /vote help
                help(user_id)
            elif text.startswith('rate'):
                # /vote rate [id] [rank(1-5)]
                vote_rate = re.findall(r'rate\s(\d{1,2})\s{1,}(\d{1,})', text)
                if vote_rate:
                    rate_vote(user_id, user, int(vote_rate[0][0]), int(vote_rate[0][1]))
                else:
                    send_404(user_id, u"Ошибка на фабрике по производству спирта")
        else:
            # /vote, /vote help
            help(user_id)
    return Response(), 200


@app.route("/api")
def api():
    u"""Входная точка API."""
    return jsonify({"data": get_sorted_votes()})


@app.route("/")
def index():
    u"""Входная точка шаблона."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
