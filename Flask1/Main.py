import flask

app = flask.Flask(__name__)


@app.route('/')
def something():
    return flask.render_template("Hello.html")

@app.route('/<name>')
def user(name):
    if name:
        return flask.render_template("Hello.html", name=name)
    else:
        return flask.abort(404)

if __name__ == "__main__":
    app.run(debug=True)
