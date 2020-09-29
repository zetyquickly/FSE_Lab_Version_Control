class Storage:
    def __init__(self, data={}):
        super().__init__()
        if isinstance(data, dict):
            self.data = data
        else:
            raise Exception

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def remove(self,key):
        if key in self.data:
            self.data.pop(key)
            return self.data
        else:
            return None
        

    def set(self):
        pass
    
    def add(self):
        pass
