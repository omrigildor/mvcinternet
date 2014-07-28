import flask, flask.views

app = flask.Flask(__name__)
app.name = "hello-world"

class HelloName(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')

    def post(self):
        return "Hello " + str(flask.request.form['GO'])

class HelloWorld(flask.views.MethodView):
    def get(self):
        return "Hello World"

app.add_url_rule('/hello-world', view_func=HelloWorld.as_view('main'),methods=["GET"])
app.add_url_rule('/hello-name', view_func=HelloName.as_view('name'), methods=["GET","POST"])

app.debug = True
app.run()