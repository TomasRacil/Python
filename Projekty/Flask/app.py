# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import datetime

# create the application object
app = Flask(__name__)

@app.route('/home')
def welcome():
    return render_template('home.html') # render a template    

@app.route('/index')
def vypis_Datum():
	date=datetime.datetime.now()
	den=format(date.day)
	mesic=format(date.month)
	rok=format(date.year)
	dnesni_Datum=den+"."+mesic+"."+rok
	dnesni_Datum=str(dnesni_Datum)
	return render_template('index.html',datum=dnesni_Datum)

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Vaše údaje nesouhlasí. Zkuste to prosím znovu.'
        else:
            return redirect(url_for('vypis_Datum'))
    return render_template('login.html', error=error)


if __name__ == '__main__': # nemusim pokazdy znovu spoustit server, kdyz provedu nejakou zmenu
    app.run(debug=True)
