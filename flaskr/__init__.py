import os

from flask import Flask

def create_app(test_config=None):
    #buat dan konfigurasi app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
            )
    
    if test_config is None:
        #meload config instance, bila ada tidak testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        #meload test config jika pass
        app.config.from_mapping(test_config)

    #memastikan folder instance ada
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # halaman sederhana say hello
    @app.route('/hello')
    def hello():
        return 'Hello Cakkk Ningg !!!'

    from . import db
    db.init_app(app)

    return app

