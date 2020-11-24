import sqlite3

import click
from flask import current_app, g #g je speciální objekt, který zajistí, že při každém requestu nebudeme znovu otevírat spojení s databází. current_app používáme, abychom mohli přistoupit k některým částem aplikace ještě předtím než byla vytovořena. Třeba k templatům nebo blueprintům.
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        ) #spojení s databází
        g.db.row_factory = sqlite3.Row # Umožňuje vracet řádky jako knihovnu.

    return g.db


def close_db(e=None): #Ukončí spojení s databází pokud bylo vytvořeno.
    db = g.pop('db', None)

    if db is not None:
        db.close()

#Následující dvě funkce se starají o vytvoření databáze pomocí námi vztvořeného schématu. První získá pomocí open_resource náš soubor se strukturou a aplikuje ho. Druhá se pak stará o spuštění prvního a kontrolu jestli byla databáze inicializována.

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f: 
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

#Následující funkce registruje funkce close_db a init_db_command pro naši aplikaci.

def init_app(app):
    app.teardown_appcontext(close_db) #Tato funkce je volána po odeslání odezvy.
    app.cli.add_command(init_db_command) #Přidává nový příkaz volatelný pomocí flasku (flask init-db).
