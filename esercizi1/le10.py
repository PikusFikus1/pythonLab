class Model():

    def __init__(self, n):
        self.n = n

    def fit(self, data):

        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):

        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    
    def predict(self, data, n):
        #logica
        newList = data[-self.n:]
        incrementSum = 0
        for i in range(0, len(newList)-1):
            incrementSum += newList[i+1]-newList[i]
            print(newList[i+1]-newList[i])
        increment = incrementSum/(self.n-1)
        prediction = newList[len(newList)-1]+increment
        return prediction

class FitIncrementModel(IncrementModel):

    def fit(self, data):
        incrementSum = 0
        for i in len(data)-1:
            incrementSum += data[i+1]-data[i]
        self.avgIncrement = incrementSum/len(data)

#list = [1,2,3,4,5,6,7]
#model = IncrementModel(4)
#print(model.predict(list, 3))
#print(model)
