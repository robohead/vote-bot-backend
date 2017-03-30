# coding=utf-8
from __future__ import unicode_literals

from vote_bot import db
from vote_bot.utils import get_vote_as_attachment
from vote_bot.utils import direct_msg
from vote_bot.utils import send_404


def show_vote(user_id, vote_id):
    """
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
        direct_msg(user_id, "Появилось новое предложение", attachments)
    else:
        send_404(user_id, "Сколько не проси, найти не могу.")
