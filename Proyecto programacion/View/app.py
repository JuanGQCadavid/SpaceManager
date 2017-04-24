from flask import Flask

app = Flask(__name__)

#Para ver en donde metemos la pata
app.debug = True

@app.route('/')
def index():
    return "Hello! "

if __name__ == "__main__":
    app.run()