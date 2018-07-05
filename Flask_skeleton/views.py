from app import app
@app.route("/")
def homePage():
    return "<h1>Hello from flask!</h1>"