




import struct 
import pickle
import socket

class AData():
    def __init__(self):
        self.__m_body : dict = None 

    @property
    def body(self):
        return self.__m_body
    
    @body.setter
    def body(self, body : dict):
        self.__m_body = body 

    def deserialize(self, socket : socket.socket):
        data = socket.recv(struct.calcsize("!Q")) # this is 8 bytes
        body_size, *_ = struct.unpack("!Q", data)
        self.body = pickle.loads(socket.recv(body_size))
        


    def serialize(self, socket : socket.socket):
        """
            return [header, body] : bytes

            header layout : 
                - data_size :  unsigned long long (8 BYTES)
                
        """
        body = pickle.dumps(self.body)
        body_size = len(body)
        info_packet = struct.pack("!Q", body_size)
        socket.send(info_packet + body)
        





    



