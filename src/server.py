import socket 
from . import constants
import logging 
import sys 
logger =logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

import pickle
import uuid

import struct

import queue 
import threading 

from . import data

class Data:
    def __init__(self):
        self.m_header = {}
        self.m_body = {}
    
    @property
    def header(self):
        self.m_header 
    
    @header.setter
    def header(self, header):
        self.m_header = header
    @property
    def body(self):
        return self.m_body
    @body.setter
    def body(self, body):
        self.m_body = body 


class ClientObject():
    def __init__(self, socket : socket.socket, addr ):
        self.m_socket = socket
        self.m_addr = addr
        self.m_uuid = uuid.uuid4()
        self.m_input_queue = queue.Queue()
        self.m_output_queue = queue.Queue()

    @property
    def uid(self):
        return self.m_uuid

    def recv(self):
        # recv header 
        logger.debug("recv header")
        new_data = data.AData()
        new_data.deserialize(self.m_socket)
        self.m_input_queue.put(new_data)
        #recv body

        

    def get_input(self, data):
        self.m_input_queue.put(data)
    
    def get(self):
        return self.m_output_queue.get(block=False)

class Server():



    
    def __init__(self, host = constants.default_host, port = constants.default_port):
        self.m_host = host 
        self.m_port = port 
        self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.m_socket.bind((self.m_host, self.m_port))
        logger.info("server started...")
        

        self.m_accepted_client_sockets = []
        self.m_listen_client_sockets = {}
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
            # clientsocket.setblocking(False)
            logger.debug("accepeted %s %s", clientsocket, address)
            logger.debug("wait on append sock info")
            self.m_lock.acquire()
            
            self.m_accepted_client_sockets.append(ClientObject(clientsocket, address))
            self.m_lock.release()
            logger.debug("new sock was appended")

    
    @property
    def host(self):
        return self.m_host 




    def _check_new_client(self):
        if self.m_lock.acquire(False) : # None blocking
            if(len(self.m_accepted_client_sockets)):
                for client in self.m_accepted_client_sockets:
                    self.m_listen_client_sockets[client.uid] = client
                self.m_accepted_client_sockets.clear()
            self.m_lock.release()
        else : 
            pass 


    def run(self):
        logger.info("start run  listen to " + str(self.m_host) +" " + str(self.m_port))
        self.m_socket.listen(constants.default_connection_size)
        self.m_listen_thread.start()

        while True :
            self._check_new_client()
            for uuid, client_object in self.m_listen_client_sockets.items():
                
                client_object.recv()



    def start(self):
        self.m_recv_thread.start()
        self.m_recv_thread.join()


if __name__ == "__main__":
    server = Server()
    server.start()