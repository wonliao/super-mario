from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

PRIZES = [100, 500, 1000, 5000, 10000]

@app.route('/')
def index():
    return render_template('index.html', prizes=PRIZES)

@app.route('/spin')
def spin():
    index = random.randrange(len(PRIZES))
    prize = PRIZES[index]
    return jsonify({'index': index, 'prize': prize})

if __name__ == '__main__':
    app.run(debug=True)
