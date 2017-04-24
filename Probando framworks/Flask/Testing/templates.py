from flask import Flask
from flask import render_template,render_template_string

#app = Flask(__name__, template_folder = 'nombreFolder')
app = Flask(__name__)

#Para ver en donde metemos la pata
app.debug = True

@app.route('/')
@app.route('/<userName>')
def index(userName = None):

	edad = 18
	lista = [1,2,3,4,5,6]
	if userName == None:
		return render_template('index.html', nombre=".")
	else:
		return render_template('index.html', nombre=userName, edad = edad, lista = lista)

@app.route('/tomates')
def tomates():
	return render_template_string(
			"""
				{% if valid %}
					<h1> Valido </h1>
				{% else %}
					<h1> Nada parse :C </h1>
				{% endif %}

			""", valid = True


		)

@app.route('/dicc')
def dicc():
	dicc = {'name':"Juan", 'ape':"Gonzalo", 'edad': 15}
	return render_template_string(
			"""
				<h1>{{dicc.name}} - {{dicc.ape}} - {{dicc.edad}}</h1>

			""", dicc = dicc


		)

@app.route('/iter')
def iter():
	dicc = [{'name':"Juan", 'ape':"Gonzalo", 'edad': 15},
			{'name':"Fernando", 'ape':"Quiroz", 'edad': 16},
			{'name':"Adriana", 'ape':"Zapata", 'edad': 17},
			{'name':"Vale", 'ape':"Cadavid", 'edad': 18},
			{'name':"kate", 'ape':"Gomez", 'edad': 19}]
	return render_template_string(
			"""
				{% for user in dicc%}
					{% if user.edad > 16%}
						<h1>{{user.name}} - {{user.ape}} - {{user.edad}}</h1>
						<br/>
					{% endif %}
				{% endfor %}
				

			""", dicc = dicc


		)

app.run()