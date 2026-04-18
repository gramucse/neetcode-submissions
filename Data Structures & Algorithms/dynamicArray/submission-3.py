class DynamicArray:
    
    
    size=0
    
    def __init__(self, capacity: int):
        self.L=[]
        self.size=capacity
        self.count=0


    def get(self, i: int) -> int:
        return self.L[i]


    def set(self, i: int, n: int) -> None:
        self.L[i]=n


    def pushback(self, n: int) -> None:
        if(self.count>=self.size):
            self.resize()
        self.L.append(n)
        self.count+=1
        print(self.L)
        



    def popback(self) -> int:
        k=self.L.pop(self.count-1)
        self.count-=1
        return k
 

    def resize(self) -> None:
        self.size*=2


    def getSize(self) -> int:
        return len(self.L)
        
    
    def getCapacity(self) -> int:
        return self.size;
