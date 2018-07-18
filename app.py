from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)

socketio = SocketIO(logger=True)


# Comment this and use ./run.sh to see that logs are back, restarting is back
socketio.init_app(app)