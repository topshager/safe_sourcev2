import os
from flask import Flask
from . import contact
from .import db
from flask import Flask, render_template, request, redirect, url_for

def create_app(test_config=None):
    #creating and configuring app
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'safe_source.sqlite'),
    )

    if test_config is None:
        #load instance config if it exists when not testing
        app.config.from_pyfile('config.py',silent=True)
    else:
        #load the test config if passed in
        app.config.from_mapping(test_config)

    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/service')
    def service():
        return render_template('service.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    db.init_app(app)

    app.register_blueprint(contact.bp)


    return app
