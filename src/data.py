




import struct 
import pickle
import socket



# header layout : 
#     - data_size :  unsigned long long (8 BYTES)
#     - message_type : 
class AData():
    def __init__(self):
        self.__m_body : dict = None 

    @property
    def body(self):
        return self.__m_body
    
    @body.setter
    def body(self, body : dict):
        self.__m_body = body 

    def deserialize(self, socket : socket.socket, unpickle_body=True):
        data = socket.recv(struct.calcsize("!Q")) # this is 8 bytes
        body_size, *_ = struct.unpack("!Q", data)

        body_data = socket.recv(body_size)
        if unpickle_body : 
            self.body = pickle.loads(body_data)
        else :
            self.body = body_data
        


    def serialize(self):
        """
            return [header, body] : bytes

            header layout : 
                - data_size :  unsigned long long (8 BYTES)
                
        """
        body = pickle.dumps(self.body)
        body_size = len(body)
        info_packet = struct.pack("!Q", body_size)
        return info_packet + body
        




class Message(AData):
    def __init__(self):
        pass 
    




    



