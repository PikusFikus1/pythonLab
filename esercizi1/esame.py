class MovingAverage():

    def __init__(self, n):
        if not type(n) is int:
            raise ExamException("Solo numeri interi")
        if n < 1:
            raise ExamException("No numeri minori a 1")
        self.n = n

    def media(self, list):
        media = sum(list)/len(list)
        return(media)
    
    def compute(self, list):
        insieme = []
        listaMedia = []
        if list == None:
            raise ExamException('None not supported')
        if list == insieme:
            raise ExamException('Lista vuota')
        if type(list) == int or type(list) == float:
            raise ExamException('List can not be int or float type')
        if self.n > len(list):
            raise ExamException("Finestra più grande della lista")
        for item in list:
            if type(item) == str:
                raise ExamException("Item can't be string")
        for i in range(len(list)-(self.n-1)):
            insieme.append([list[i] for i in range(self.n)])
            list.pop(0)
        listaMedia = [self.media(item) for item in insieme]
        return listaMedia

class ExamException(Exception):
    pass
    
#moving_average = MovingAverage(-2)
#result = moving_average.compute([1,1,2,3,4,5])
#print(result)