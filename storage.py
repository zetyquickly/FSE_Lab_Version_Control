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

    def add(self, key, value):
        if key in self.data:
          raise KeyError("Key already exists")
        else:
          self.data[key] = value

    def remove(self, key):
        if key in self.data:
        	del self.data[key]
        	return self
        else:
        	raise KeyError("key not found")

    def set(self, key, value):
        if key in self.data:
            self.data[key] = value
        else: raise Exception
    