class Diff():

    def __init__(self, ratio=1):
        if type(ratio) != int and type(ratio) != float:
            raise ExamException('Ratio not a number')
        if ratio <= 0:
            raise ExamException('No negative ratio')
        self.ratio=ratio

    def compute(self,list):
        if list == None:
            raise ExamException('None not valid')
        if type(list) == int or type(list) == float or type(list) == list:
            raise ExamException('List is not a list')
        if len(list) <= 1:
            raise ExamException('List not long enough')
        for item in list:
            if type(item) == str:
                raise ExamException("Item can't be string")
        differenze = [(list[i+1]-list[i])/self.ratio for i in range(len(list)-1)]
        return differenze
        

class ExamException(Exception):
    pass

#diff = Diff()
#lista = diff.compute([1])
#print(lista)