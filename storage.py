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

    def remove(self):
        pass

    def set(self):
        pass
    
    def add(self, key, value):
        if key in self.data:
            return 404 # unsuccess code
        else:
            self.data[key] = value
            return 0 # success code
