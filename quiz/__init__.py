import os

from flask import Flask

def create_app(app_name='QUIZ'):
    app = Flask(app_name)
#   __name__, instance_relative_config=True)
    app.config.from_object('quiz.config.BaseConfig')
#    if test_config is None:
#        # load the instance config, if it exists, when not testing
#        app.config.from_pyfile('config.py', silent=True)
#    else:
#        # load the test config if passed in
#        app.config.from_mapping(test_config)

#    ensure the instance folder exists
#    try:
#        os.makedirs(app.instance_path)
#    except OSError:
#        pass
#

    from quiz.api import api
    app.register_blueprint(api, url_prefix="/api")

    from quiz.models import db 
    db.init_app(app)
    return app
