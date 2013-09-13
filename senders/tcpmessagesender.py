import socket
import time


class TCPMessageSender:
    def __init__(self, SERVER_ADDR, log, reconnect=True, connect=True):
        self.SERVER_ADDR = SERVER_ADDR
        self.reconnect = reconnect
        self.RECV_BUFFER_SIZE = 4096
        if connect:
            self.connect()

    def send(self, data):
        try:
            self.socket.send(data)
            response = self.socket.recv(self.RECV_BUFFER_SIZE)
        except IOError as e:
            log(e)
            if e.errno == 32 and self.reconnect is True:
                log('Reconnecting...')
                connected = self.connect()
                if connected is True:
                    log("Resending...")
                    response = self.send(data)
            response = ''
        return response

    def connect(self):
        connected = False
        while connected is False:
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect(self.SERVER_ADDR)
                connected = True
            except IOError as e:
                if self.reconnect is False:
                    break
                print e, self.SERVER_ADDR
                time.sleep(1)
        if connected is False:
            log("Not Connected")
        else:
            log("Connected")
        return connected
