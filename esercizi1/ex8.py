class Model():

    def __init__(self, name=''):
        self.name = name

    def fit(self,data):

        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):

        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def predict(self, data):
        prevValue = None
        totVar = 0
        for i,item in data:
            if i == 0:
                prevValue = item
            else:
                totVar += item-prevValue
                prevValue = item
        return totVar/(len(data)-1)

list = {50,52,60}
myList = IncrementModel('test.csv')
print(myList.predict(list))
