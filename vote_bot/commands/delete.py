# coding=utf-8
from __future__ import unicode_literals

from vote_bot import db
from vote_bot.utils import direct_msg
from vote_bot.utils import send_404


def delete_vote(user_id, vote_id):
    """
    Удаляет предложение.

    Такая возможность должна быть только у автора предложения.

    команда: /vote delete [id]
    """
    vote = db.get(eid=vote_id)
    if vote and user_id == vote['author_id']:
        db.remove(eids=[vote_id])
        attachments = [
            {"color": "good", "title": "#%d %s" % (vote.eid, vote['content'])}]
        direct_msg(user_id, "Предложение удалено", attachments)
    else:
        send_404(user_id, "Не могу удалить то, чего нет")
