# coding=utf-8
import os

from flask import Flask
from slackclient import SlackClient
from tinydb import TinyDB

DOMAIN = os.environ.get('DOMAIN', 'external-url-of-this-bot')
SLACK_TOKEN = os.environ.get('SLACK_TOKEN', '')
SLASH_COMMANDS_TOKEN = os.environ.get('SLASH_COMMANDS_TOKEN', '')
DEFAULT_CHANNEL = os.environ.get('DEFAULT_CHANNEL', 'general')

app = Flask(__name__, static_url_path='')
slack_client = SlackClient(SLACK_TOKEN)
db = TinyDB('db.json')

import vote_bot.views  # noqa
