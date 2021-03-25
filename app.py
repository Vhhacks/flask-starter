from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Implementing marine life sightings

# Orca
# http://hotline.whalemuseum.org/api.json?species=orca&near=49.203579,%20-122.850776&radius=10

# Dolphin
# http://hotline.whalemuseum.org/api.json?species=pacific%20white-sided%20dolphin&near=49.203579,%20-122.850776&radius=1

# Seal
# http://hotline.whalemuseum.org/api.json?species=harbor%20seal&near=49.203579,%20-122.850776&radius=1

# Maps link:
# http://www.google.com/maps/place/49.46800006494457,17.11514008755796

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