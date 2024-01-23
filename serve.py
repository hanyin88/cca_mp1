from flask import Flask, request
import socket
import subprocess


app = Flask(__name__)
seed_value =100

@app.get('/')
def get_socket():
    return socket.gethostname()

@app.post('/')
def update_seed():
    subprocess.Popen(["python", "stress_cpu.py"])
    return "stress test with cpu started"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)