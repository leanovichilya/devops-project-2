from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
  return "<h1>Hello, World!</h1>"

@app.route("/home")
def get_data():
  user_data = {
    "status": "ok"
  }

  return jsonify(user_data)
  # return user_data

@app.route("/about")
def about():
  return 'This is the about page.'

@app.route("/contact")
def contact():
  return 'This is the contact page.'

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
