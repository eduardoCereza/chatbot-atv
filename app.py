from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)

mensagem = ''

@app.route("/chat", methods=['GET'])
def render_page():
    return render_template('index.html',
                           host='http://127.0.0.1:5000')

@socketio.on('message')
def post_message(msg):
    
    if not msg:
        return
    
    
    socketio.send(msg)
    
    
    
    

@socketio.on('disconnect')
def handle_disconnect():
    print("Client has disconnected to the server!")

if __name__ == "__main__":
    socketio.run(app, debug=True)