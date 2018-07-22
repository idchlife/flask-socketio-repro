from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from eventlet import monkey_patch

monkey_patch()


app = Flask(__name__)

"""
UNCOMMENT ONE OF THE SCENARIOS CODES AND COMMENT OTHERS TO TEST
"""

"""SCENARIO 1
message_queue in constructor and in .init_app

Client is not receiving custom events
"""
#socketio = SocketIO(message_queue="redis://")
#socketio.init_app(app, message_queue="redis://")

"""SCENARIO 2
message_queue in constructor only

Client is not receiving custom events
"""
# socketio = SocketIO(message_queue="redis://")
# socketio.init_app(app)

"""SCENARIO 3
message_queue in init_app

Client is receiving events as it should
"""
socketio = SocketIO()
socketio.init_app(app, message_queue="redis://")

@app.route("/")
def test_socket():
  return render_template("test-socket.html")


@socketio.on("custom_ping")
def ping():
  print("PINGED!")
  emit("custom_pong", {'data': 2323})

@socketio.on("connect")
def on_connect():
  print("Someones connected! Sending bacj")
  emit("custom", {'data': 2323})
  socketio.emit("custom", "well")