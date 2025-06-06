from flask import Flask, render_template, jsonify
import random
from datetime import datetime
import json
import os

app = Flask(__name__)

SPIN_LOG_FILE = 'spin_log.txt'
with open(SPIN_LOG_FILE, 'a', encoding='utf-8'):
    pass

PRIZES = [100, 500, 1000, 5000, 10000, 20000, 50000, 100000, 200000, 1000000]

@app.route('/')
def index():
    return render_template('index.html', prizes=PRIZES)

@app.route('/spin')
def spin():
    index = random.randrange(len(PRIZES))
    prize = PRIZES[index]
    log_entry = {'time': datetime.now().isoformat(), 'prize': prize}
    with open(SPIN_LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(json.dumps(log_entry) + '\n')
    return jsonify({'index': index, 'prize': prize})


@app.route('/results')
def results():
    if not os.path.exists(SPIN_LOG_FILE):
        return jsonify([])
    with open(SPIN_LOG_FILE, 'r', encoding='utf-8') as f:
        logs = [json.loads(line) for line in f if line.strip()]
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)
