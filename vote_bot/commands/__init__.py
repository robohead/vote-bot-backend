# coding=utf-8
# flake8: noqa
from .add import add_vote
from .delete import delete_vote
from .help import help
from .list import list_votes
from .rate import rate_vote
from .show import show_vote
from .update import update_vote


def call_command(text, user, user_id):
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
