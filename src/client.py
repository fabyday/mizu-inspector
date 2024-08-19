import socket 
from . import constants
import logging 
import pickle

import queue


default_logger = logging.getLogger()

from . import data


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
        i = 0
        while True:
            # item = self.m_write_buffer.get()
            new_data = data.AData()
            new_data.body = {"integer" : i }
            print("send")
            new_data.serialize(self.m_socket)
            i+= 1

if __name__ == "__main__":

    a = Client()
    a.start()