import socket
import multiprocessing as mp
import os


HOST = ''
PORT = 9999
END = ['/end', '/close', '/terminate']


class server:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))
        self.s.listen(5)
        self.list = []
        

    def wait_for_client(self):
        c,a = self.s.accept()
        self.list.append(c)
        return c


    def get_name(self, client):
        return client.recv(1024)


    def chat(self, client):
        #get name of the client
        name = self.get_name(client)

        while True:
            data = client.recv(1024)
            message = None
            message = (name + " : " + data)
            #terminate connection if users  wishes to
            if data in END:
               client.close()
               return

            print(message)

            #do something here to send all message to clients
            self.send_message(message)


    def send_message(self, message):
        for x in self.list:
            x.send(message)

    def start(self):
        while True:
            client = self.wait_for_client()
            process = mp.Process(target = self.chat, args = ((client,)))
            process.start()

if __name__=='__main__':
    foo = server()
    foo.start()
