from flask import Flask, render_template, jsonify

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/api/player', methods=["POST"])
def player():
    data = {"test": 69}
    return jsonify(data)

if __name__ == '__main__':
    app.run()
