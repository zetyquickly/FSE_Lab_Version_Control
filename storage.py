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

    def remove(self, key):
        if key in self.data.keys():
            del self.data[key]
        else:
            raise Exception(f'Key "{key}" does not belong to dictionary')
    
    def add(self,key,value):
        if key not in self.data.keys():
            self.data[key] = value
        else:
            raise Exception(f'Key "{key}" is already here')
    
    def set(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            return None
