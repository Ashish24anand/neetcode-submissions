class LinkedList:
    
    def __init__(self):
        self.data = []
        self.next = []

    
    def get(self, index: int) -> int:
        if index > len(self.data)-1:
            return -1
        else:
            return self.data[index]

        

    def insertHead(self, val: int) -> None:
        self.next = self.data + [None]
        self.data = [val] + self.data
        

    def insertTail(self, val: int) -> None:
        self.data = self.data + [val]
        self.next = self.data + [None]
        

    def remove(self, index: int) -> bool:
        if index < len(self.data):
            self.data.pop(index)
            self.next.pop(index)
            return True
        else:
            return False

        

    def getValues(self) -> List[int]:
        return self.data
        
