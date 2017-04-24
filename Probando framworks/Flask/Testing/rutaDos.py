from flask import Flask

app = Flask(__name__)

app.debug = True

@app.route('/')
def index():
	return 'Sap Nigga'

@app.route('/user/')
@app.route('/user/<name>')
@app.route('/user/<name>/<lastname>')
@app.route('/user/<name>/<lastname>/<int:numeroFavorito>')
def user(name = 'nadie',lastname = 'De la familia naide!', numeroFavorito = 5):
	return '<h1>Welcome {} {} {}.</h1>'.format(name, lastname, numeroFavorito)


app.run()