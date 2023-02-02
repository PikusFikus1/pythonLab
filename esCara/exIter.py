class Primo():

    def __init__(self, high):
        self.high = high

    def __iter__(self):
        self.n = 2
        return self

    def __next__(self):
        if self.n < self.high:
            pot = self.n
            self.n = self.primo(self.n)
            return pot
            
        else:
            raise StopIteration

    def primo(self,n):
        n = n+1
        while True:
            flag = False
            for i in range(2,n):
                if n%i==0:
                    flag = True
        if flag==False:
            return n
        n = n+1

pri = Primo(8)

for i in range(8):
    print(pri.__next__())
