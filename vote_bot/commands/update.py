# coding=utf-8
from __future__ import unicode_literals

from vote_bot import db
from vote_bot.utils import send_404
from vote_bot.utils import direct_msg


def update_vote(user_id, vote_id, text):
    """
    Обновляет текст предложения.

    Такая возможность должна быть только у автора предложения.

    команда: /vote update [id] [text]
    """
    vote = db.get(eid=vote_id)
    if vote:
        if user_id == vote['author_id']:
            db.update({'content': text}, eids=[vote.eid])
            attachments = [
                {"title": u"#%d %s" % (vote.eid, text), "color": "good"}]
            direct_msg(user_id, "Предложение обновлено", attachments)
        else:
            send_404(user_id, "А-та-та обновлять чужие предложения")
    else:
        send_404(user_id, "Я пьян и не могу найти предложение с таким номером")
