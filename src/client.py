import socket 
from . import constants
import logging 
import pickle

import queue
import threading


default_logger = logging.getLogger()

from . import data


class Client():
    def __init__(self, host = constants.default_host, port =  constants.default_port, clientname=""):
        self.m_host = host 
        self.m_port = port 
        self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        default_logger.info("bind")

        self.m_run_on_thread = True    

        self.m_socket.setblocking(False) # Non-blocking socket


        self.m_read_buffer = queue.Queue()

        self.m_write_buffer = queue.Queue()


        self.m_thread = threading.Thread(None, self.run, "network_io thread")


    @property
    def is_ran_on_thread(self):
        return self.m_run_on_thread
    
    @is_ran_on_thread.setter
    def is_ran_on_thread(self, flag):
        self.m_run_on_thread


    def send(self, message):
        pass


    def run(self):
        while True :
            # new_data = data.AData()

            self.__recv()
            self.__send()
            new_data.body = {"integer" : i }
            print("send")
            raw_packet = new_data.serialize()
            self.m_socket.send(raw_packet)
            i+= 1
 



    
    


    def __recv(self):
        if self.m_tmp_recv_data is None :
            self.m_tmp_recv_data = data.AData()
        buf +=  self.m_socket.recv(1000)
        self.deserialize(buf)




    def __send(self):
        pass 




    @property
    def host(self):
        return self.m_host 

    
    def start(self):
        self.m_socket.connect((self.m_host, self.m_port))
        i = 0
        self.m_thread.start()
            # item = self.m_write_buffer.get()

if __name__ == "__main__":

    a = Client()
    a.start()