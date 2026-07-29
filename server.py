from flask import Flask, request, jsonify, send_file, send_from_directory
import json
import os

BASE = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE, 'data.json')
app = Flask(__name__)

@app.route('/api/data')
def get_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    return jsonify({'credits': [], 'payments': {}})

@app.route('/api/data', methods=['POST'])
def save_data():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'invalid json'}), 400
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return jsonify({'ok': True})

@app.route('/')
def index():
    return send_file(os.path.join(BASE, 'index.html'))

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(BASE, path)

@app.after_request
def add_headers(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return resp

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
