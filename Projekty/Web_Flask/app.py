# načtení potřebných modulů a funkcí
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import datetime
import os

app = Flask(__name__) # vytvoření objektu aplikace
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!' # nastavení klíče
path=os.path.dirname(os.path.abspath(__file__)).replace("\\","/") # adresní cesta k databázi
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path}/database.db'
bootstrap = Bootstrap(app) # deklarace bootstrap
db = SQLAlchemy(app) # deklarace databáze
login_manager = LoginManager() #login_manager provádí funkci LoginManager
login_manager.init_app(app) # inicializace app
login_manager.login_view = 'login'

class User(UserMixin, db.Model): # vytvoření třídy uživatel, která obsahuje položky username,email, password a přistupuje k databázi
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader # načtení uživatelů podle user_id
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm): #vytvoření přihlašovacího formuláře pomocí modulu FlaskForm
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm): #vytvoření registračního formuláře pomocí modulu FlaskForm
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route('/') # při zadání adresy lokálního serveru a znaku / se spustí funkce index a vykreslí stránku index.html, 
def index():
    date=datetime.datetime.now()
    den=format(date.day)
    mesic=format(date.month)
    rok=format(date.year)
    dnesni_Datum=den+"."+mesic+"."+rok
    dnesni_Datum=str(dnesni_Datum)
    return render_template('index.html',datum=dnesni_Datum) # při vykreslení předáváme parametr datum, díky kterému na dané stránce proběhne funkce tam kde předáme parametr do dvojitých složených závorek

@app.route('/login', methods=['GET', 'POST']) # při adrese /login se spustí funkce login
def login():
    form = LoginForm()

    if form.validate_on_submit(): # kontrola platnosti údajů
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))

        return '<h1>Neplatné uživatelské jméno nebo heslo</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form) 

@app.route('/signup', methods=['GET', 'POST']) # při adrese /signup se spustí funkce signup pro registraci
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256') # možnost vygenerování hesla
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password) # deklarace nového uživatele
        db.session.add(new_user) # přidá nového uživatele do databáze
        db.session.commit()

        return '<h1>Nový uživatel  vytvořen!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('reg.html', form=form)


@app.route('/logout') # funkce logout provádí odhlášení, využívá přímo funkci logout_user z modulu flask_login 
@login_required
def logout():
    logout_user()
    return redirect(url_for('index')) # provedení přesměrování na stránku index.html pomocí volání funkce index 

if __name__ == '__main__': #zapnutí debug modu
    app.run(debug=True)
