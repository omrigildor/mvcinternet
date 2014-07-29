import flask, flask.views

app = flask.Flask(__name__)
app.name = "hello-world"

@app.route("/", defaults={'path':''})
@app.route("/Hello-<path:path>")
def catch_all(path):
    if path == "":
        return "Hello World"
    else:
        return "Hello " + path

def get():
    return catch_all()

app.debug = True
app.run()
