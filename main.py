from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('connect')
def connect():
    print('client connected')

@socketio.on('disconnect')
def disconnect():
    print('client disconnected')

@socketio.on('mount')
def sendmessage():
    while True:
        socketio.emit('data' , [1, 2, 3])
        socketio.sleep(2)

if __name__ == '__main__':
    socketio.run(app, port=5000)
