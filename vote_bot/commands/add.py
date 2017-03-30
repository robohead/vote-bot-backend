# coding=utf-8
from __future__ import unicode_literals

from vote_bot import db
from vote_bot import DEFAULT_CHANNEL
from vote_bot import DOMAIN
from vote_bot.utils import get_members
from vote_bot.utils import direct_msg


def add_vote(user_id, user, text):
    """
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
            "author_name": 'Автор: @' + user,
            "color": "good",
            "footer": "Проголосуй c помощью команды /vote rate [id] [1-5]"
        }, {
            "title": "Список всех предложений", "title_link": DOMAIN
        }
    ]
    if members:
        for user in members:
            direct_msg(user, "Появилось новое предложение", attachments)
