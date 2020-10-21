from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify({"a": 1})

if __name__ == "__main__":
    app.run(debug=True)