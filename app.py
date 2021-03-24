from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/assets/<path>')
def send_assets(path):
    return send_from_directory('assets', path)

@app.route('/css/<path>')
def send_style(path):
    return send_from_directory('css', path)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")