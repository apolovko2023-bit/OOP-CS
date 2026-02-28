class ListInfo:
    def __init__(self, data):
        self.data = data

    @property
    def length(self):
        return len(self.data)


numbers = [1, 2, 3, 4, 5]
obj = ListInfo(numbers)

print(obj.length)  
