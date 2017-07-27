# channels_example
A WebSocket Example Using Django Channels

# usage
1. clone this project
2. run `buildout` (you should install zc.buildout first)
3. run `bin/django runserver` to start project
4. open `http://localhost:8000/` with your browser
5. while you want see the WebsocketBinding results, you should request `http://localhost:8000/intval/?val=NEW_INT` to add a new integer into database

# reference
1. https://realpython.com/blog/python/getting-started-with-django-channels/
2. https://channels.readthedocs.io/en/stable/