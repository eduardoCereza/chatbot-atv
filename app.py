from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print("Client connected to the server!")
    

@socketio.on('disconnect')
def handle_disconnect():
    print("Client has disconnected to the server!")

if __name__ == "__main__":
    socketio.run(app, debug=True)