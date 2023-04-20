import json 

class Message():

    data = {}

    def __init__(self) -> None:
        with open("message.json", "r", encoding='utf8') as read_file:
            self.data = dict(json.load(read_file))
    
    def get_any(self, any: str): 
        return self.data.get(any)

    def get_register(self): 
        return self.data.get('validation').get('register')
    
    def get_login(self):
        return self.data.get('validation').get('login')