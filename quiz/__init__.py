import os

from flask import Flask

def create_app(app_name='QUIZ', test_config=None):
    app = Flask(app_name)

    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_object('quiz.config.BaseConfig')

    from quiz.api import api
    app.register_blueprint(api, url_prefix="/api")

    from quiz.models import db
    db.init_app(app)
    return app
