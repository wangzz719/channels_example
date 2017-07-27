#!/usr/bin/python
# -*-coding: utf8-*-
import json
from channels import Group
from channels.auth import channel_session_user_from_http, channel_session_user
from channels.generic.websockets import WebsocketDemultiplexer
from models import IntegerValueBinding


@channel_session_user_from_http
def ws_connect(message):
    Group('users').add(message.reply_channel)
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': True
        })
    })


@channel_session_user
def ws_disconnect(message):
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': False
        })
    })
    Group('users').discard(message.reply_channel)


class Demultiplexer(WebsocketDemultiplexer):

    consumers = {
        "intval": IntegerValueBinding.consumer,
    }

    def connection_groups(self):
        return ["intval-updates"]
