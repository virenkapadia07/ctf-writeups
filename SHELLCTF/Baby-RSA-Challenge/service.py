#!/bin/usr/python3
from flask import Flask, jsonify
from Crypto.Util.number import long_to_bytes
from Hidden.secret import flag

n = 12061805802038279471
e = 13

app = Flask(__name__)

def verify(sign):
    data = pow(sign,e,n)
    return long_to_bytes(data)

@app.route('/api/Baby-RSA-challenge/<int:signed_data>', methods=['GET'])
def get_tasks(signed_data):
    if(verify(signed_data) == "admin".encode()):
        return jsonify({'flag': flag})
    else:
        return jsonify({'error':'invalid input!'})

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=6660)