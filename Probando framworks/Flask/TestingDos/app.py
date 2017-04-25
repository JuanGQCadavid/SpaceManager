from flask import Flask, render_template
from flask import request

import form
app = Flask(__name__)
app.debug = True

@app.route('/',methods = ['GET','POST'])
def index():
	commetn_form = form.comentForm(request.form)

	if request.method == 'POST':
		print commetn_form.usuario.data
		print commetn_form.email.data
		print commetn_form.comentario.data

	title = "La perra valiente"
	return render_template('index.html',title = title, form = commetn_form)

app.run()