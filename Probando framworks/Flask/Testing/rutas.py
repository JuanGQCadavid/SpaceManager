from flask import Flask
from flask import request

app = Flask(__name__)

#Para ver en donde metemos la pata
app.debug = True

@app.route('/')
def index():
    return "Hello, Mejoro la mondana jajajaj "

 
"http://127.0.0.1:5000/params?params1=578&params2=878"
@app.route('/params')
def params():
    param = request.args.get('params1','No contiene')
    param_Dos = request.args.get('params2','No contiene')
    return 'El parametro es {} y {}'.format(param,param_Dos)

if __name__ == "__main__":
    app.run()


    '''''''''
    parametros 

    ?jfjosdfgsg

    from flask import request

    app.route('/params')
    '''''''''
