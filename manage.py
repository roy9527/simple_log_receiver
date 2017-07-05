#!/usr/bin/env python
import os
from app import create_app
from flask_script import Manager, Shell, Server
import logging

from flaskext.markdown import Markdown
from flask import render_template

app = create_app('debug')
Markdown(app)
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
    return render_template('ouo.html')

if __name__ == '__main__':
    # logger = logging.getLogger('gunicorn.access')
    # logger.addHandler(WatchedFileHandler('log/gunicorn_access.log'))
    # logger.propagate = False
    manager.run()