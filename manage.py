#!/usr/bin/env python
import os
from app import create_app
from flask_script import Manager, Shell, Server
import logging

app = create_app('debug')
manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(app=app)

manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '127.0.0.1')
)


@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    handler = logging.FileHandler('eiffel_flask.log', encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter('%(asctime)s - %(funcName)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    manager.run()