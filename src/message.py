import pickle 

class Message:
    def __init__(self):
        self.m_header = None
        self.m_body = None 



    @property
    def header(self):
        return self.m_header 



    @property()
    def body(self):
        return self.m_body


    def to_bytes(self):

        return pickle.dumps(self.m_header), pickle.dumps(self.m_body)
    
