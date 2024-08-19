import socket 
from . import constants
import logging 


import sys 
logger =logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

import pickle


import queue 
import threading 

class Server():



    
    def __init__(self, host = constants.default_host, port = constants.default_port):
        self.m_host = host 
        self.m_port = port 
        self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.m_socket.bind((self.m_host, self.m_port))
        logger.info("server started...")
        

        self.m_accepted_client_sockets = []
        self.m_listen_client_sockets = []
        self.received_queue = queue.Queue()


        self.m_listen_thread = threading.Thread(target = self.__listen, name="listen")
        self.m_listen_thread.daemon = True 
        self.m_recv_thread = threading.Thread(target = self.run, name="recv")
        self.m_recv_thread.daemon = True
        self.m_lock  =threading.Lock()


    def __listen(self):

        logger.info("start listen thread")
        while True : 

            logger.debug("wait to accept")
            clientsocket, address = self.m_socket.accept()
            logger.debug("accepeted %s %s", clientsocket, address)
            logger.debug("wait on append sock info")
            self.m_lock.acquire()
            self.m_accepted_client_sockets.append((clientsocket, address))
            self.m_lock.release()
            logger.debug("new sock was appended")

    
    @property
    def host(self):
        return self.m_host 




    def _check_new_client(self):
        self.m_lock.acquire()
        if(len(self.m_accepted_client_sockets)):
            self.m_listen_client_sockets += self.m_accepted_client_sockets 
            self.m_accepted_client_sockets.clear()
        self.m_lock.release()


    def run(self):
        logger.info("start run  listen to " + str(self.m_host) +" " + str(self.m_port))
        self.m_socket.listen(constants.default_connection_size)
        self.m_listen_thread.start()

        while True :
            self._check_new_client()

            for socks in self.m_listen_client_sockets:
                client_sock, address = socks
                pickle.loads(client_sock.recv(1024))


    def start(self):
        self.m_recv_thread.start()
        self.m_recv_thread.join()


if __name__ == "__main__":
    server = Server()
    server.start()