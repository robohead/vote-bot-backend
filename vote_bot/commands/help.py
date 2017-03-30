# coding=utf-8
from __future__ import unicode_literals

from vote_bot.utils import direct_msg


def help(user_id):
    """
    Выводит список команд и полезную информацию о команде

    команда: /vote, /vote help
    """
    text = """
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
