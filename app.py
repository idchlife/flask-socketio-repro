from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit


app = Flask(__name__)

socketio = SocketIO(logger=True)

@app.route("/")
def test_socket():
  return render_template("test-socket.html")


@socketio.on("connect")
def on_connect():
  print("Someones connected! Sending bacj")
  emit("message", { 'msg': "HELLO" })

@socketio.on("ping")
def ping():
  print("PINGED!")
  emit("message", { 'msg': "PONG" })

socketio.init_app(app)