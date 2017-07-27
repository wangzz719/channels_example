#!/usr/bin/python
# -*-coding: utf8-*-

from channels.routing import route
from channels import route_class
from example.consumers import ws_connect, ws_disconnect, Demultiplexer


channel_routing = [
    route('websocket.connect', ws_connect, path="^/users/"),
    route('websocket.disconnect', ws_disconnect, path="^/users/"),
    route_class(Demultiplexer, path="^/binding/")
]
