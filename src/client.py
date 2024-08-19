import socket 
from . import constants
import logging 
import pickle

import queue


default_logger = logging.getLogger()




class Client():
    def __init__(self, host = constants.default_host, port =  constants.default_port, clientname=""):
        self.m_host = host 
        self.m_port = port 
        self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        default_logger.info("bind")

        self.m_run_on_thread = True 


        self.m_read_buffer = queue.Queue()

        self.m_write_buffer = queue.Queue()


    @property
    def is_ran_on_thread(self):
        return self.m_run_on_thread
    
    @is_ran_on_thread.setter
    def is_ran_on_thread(self, flag):
        self.m_run_on_thread


    def send(self, message):
        pass


    def run(self):
        pass 



    
    

        



    @property
    def host(self):
        return self.m_host 

    
    def start(self):
        self.m_socket.connect((self.m_host, self.m_port))
        while True:
            item = self.m_write_buffer.get()
            self.m_socket.send(b"test")

if __name__ == "__main__":

    a = Client()
    a.start()