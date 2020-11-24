
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True) #Určujeme knihovnu, z které bude Flask čerpat při vytváření aplikace.
    app.config.from_mapping( 
        SECRET_KEY='dev', 
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), #Tímto příkazem nastavíme cestu k databázi, do které budeme ukládat vše potřebné používáme. sqlite neboť je vestavěno do základní 
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Přidá funkce z knihovny db kterou jsme vytvořili.
    from . import db
    db.init_app(app)

    # Přidá blueprint pro authorizaci.

    from . import auth
    app.register_blueprint(auth.bp)

    # Přidá blueprint pro blog.

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app