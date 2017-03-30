# coding=utf-8
from __future__ import unicode_literals

from vote_bot import db
from vote_bot import slack_client
from vote_bot import SLASH_COMMANDS_TOKEN


BOT_USERNAME = "Scorpion"
DEFAULT_KWARGS = {
    "username": BOT_USERNAME,
    "icon_url": "http://www.jogosonlinepc.com.br/imagens_posts/fotoscorpion.jpg",
    "response_type": "ephemeral",
}


def get_sorted_votes(index=None):
    """Возвращет отсортированный по райтингу результат."""
    return sorted(db.all(), key=lambda x: x['rank'], reverse=True)[:index]


def get_vote_as_attachment(user, vote_id, vote_content, vote_rank, voters):
    """Возвращает отформатированный объект предложения."""
    return {
        "author_name": "Автор: @%s" % user,
        "title": "#%d %s" % (vote_id, vote_content),
        "color": "good",
        "footer": "Ранк: %d\nПроголосовавшие: %s" % (vote_rank, ', '.join(voters))
    }


def get_members(channel_id):
    """Получает список пользователей из канала."""
    data = slack_client.api_call(
        "channels.info",
        token=SLASH_COMMANDS_TOKEN,
        channel=channel_id
    )
    if data.get('channel'):
        return data['channel'].get('members')


def send_404(user_id, text):
    """Отправляет сообщение об ошибке."""
    direct_msg(user_id, None, [{"text": text, "color": "danger"}])


def direct_msg(user_id, text=None, attachments=None):
    """Отправляет сообщение в канал slackbot."""
    kwargs = DEFAULT_KWARGS
    kwargs['channel'] = user_id
    if text:
        kwargs['text'] = text
    if attachments:
        kwargs['attachments'] = attachments
    slack_client.api_call("chat.postMessage", **kwargs)
