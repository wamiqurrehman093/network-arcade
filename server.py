import socket
from _thread import *
import sys
from player import Player
import pickle
from variables import *

f = open("server_ip.txt", 'r')
f1 = f.readline()
# server = "192.168.10.170"
server = f1
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("waiting for a connection, server started")

players = [Player(0, 0, 50, 50, RED), Player(100, 100, 50, 50, GREEN)]

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            if not data:
                print("disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("received: ", data)
                print("sending: ", reply)
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("lost connection")
    conn.close()

currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("connected to: ", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
