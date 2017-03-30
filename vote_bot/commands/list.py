# coding=utf-8
from __future__ import unicode_literals

from vote_bot.utils import get_sorted_votes
from vote_bot.utils import get_vote_as_attachment
from vote_bot.utils import direct_msg


def create_attachment(vote):
    return get_vote_as_attachment(
        vote['author_name'], vote.eid, vote['content'],
        vote['rank'], vote.get('voters', '-'))


def list_votes(user_id):
    """
    Выводит список предложений начиная с самого высокого ранга.

    команда: /vote list
    """
    # Берем первые десять
    votes = get_sorted_votes(10)
    attachments = [create_attachment(vote) for vote in votes]
    direct_msg(user_id, u"Список предложений:", attachments)
