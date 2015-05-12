import socket

HOST = '127.0.0.1'
PORT = 9999
END = ['/end', '/close', '/terminate']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

if __name__=='__main__':
     name = raw_input("Enter your name")
     s.send(name)

     while True:
          message = raw_input()
          if message in END:
             break
          s.send(message)
          data = s.recv(1024)
          print(data)
