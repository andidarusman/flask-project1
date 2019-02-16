import os

from flask import Flask

def create_app():
    app = ...
    #sek ya

    from . import auth
    app.register_blueprint(auth.bp)

    return app

