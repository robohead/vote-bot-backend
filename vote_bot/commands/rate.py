from __future__ import unicode_literals

from vote_bot import db
from vote_bot.utils import direct_msg
from vote_bot.utils import send_404
from vote_bot.utils import get_vote_as_attachment


def rate_vote(user_id, user, vote_id, rank):
    """
    Проголосовать за предложение.

    команда: /vote rate [id] [1-5]
    """
    if rank in range(1, 6):
        vote = db.get(eid=vote_id)
        if vote:
            voters = vote['voters']
            if user in voters:
                # Пользователь уже голосовал за предложение
                send_404(
                    user_id,
                    "https://ru.wikipedia.org/wiki/%D0%90%D0%BC%D0%BD%D0%B5%D0%B7%D0%B8%D1%8F")
            else:
                rank = vote['rank'] + rank
                voters = voters + [user]
                db.update({"rank": rank, "voters": voters}, eids=[vote_id])
                attachments = [
                    get_vote_as_attachment(user, vote.eid,
                    vote['content'], rank, voters)]
                direct_msg(user_id, "Голос принят", attachments)
        else:
            send_404(
                user_id,
                "Ты уверен что твое сознание безгранично и есть бытие?")
    else:
        send_404(
            user_id,
            "А-та-та, проголосовать можно только значением от 1-го до 5-ти.")
