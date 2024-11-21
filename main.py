from flask import Flask, jsonify

import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'message': f'The time now is: {datetime.datetime.now()}'})

@app.route('/About_me')
def About_me():
    return jsonify({'message': 'I am Sameeksha!'})


if __name__ == '__main__':
    app.run(debug=True)
