from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, rooms

app = Flask(__name__)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

@socketio.on('playPressed')
def playPressed(message):
    socketio.emit("playPressed", "play the video", room=message["code"])

@socketio.on('pausePressed')
def pausePressed(message):
    socketio.emit("pausePressed", "play the video", room=message["code"])

@socketio.on('timeUpdate')
def timeUpdate(message):
    socketio.emit("timeUpdate", [message["newTime"], message["emitter"]], room=message["code"])

@socketio.on('chat')
def chat(message):
    socketio.emit("chat_message", message["message"], room=message["code"])

@socketio.on('joinRoom')
def joinRoom(message):
    join_room(message["code"])

@app.route('/')
def home():
    return "hi!"

if __name__ == "__main__":    
    socketio.run(app, host="0.0.0.0", debug=True)
