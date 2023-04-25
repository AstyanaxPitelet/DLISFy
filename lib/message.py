import json 

class Message():

    data = {}

    def __init__(self) -> None:
        with open("message.json", "r", encoding='utf8') as read_file:
            self.data = dict(json.load(read_file))
    
    def get_default(self): 
        return self.data.get('default')

    def get_register(self): 
        return self.data.get('validation').get('register')
    
    def get_login(self):
        return self.data.get('validation').get('login')