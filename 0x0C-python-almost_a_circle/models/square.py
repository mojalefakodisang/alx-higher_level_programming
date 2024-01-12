from models.rectangle import Rectangle


class Square(Rectangle):
    
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
        
    def __str__(self):
        return ("[{}] ({}) {}/{} - {}".
                format("Square", self.id, self.x, self.y, self.width))
        
    def update(self, *args, **kwargs):
        if len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
                    
    def to_dictionary(self):
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }