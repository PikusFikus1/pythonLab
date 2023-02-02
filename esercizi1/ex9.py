class Model():

    def __init__(self, name):
        self.name = name

    def fit(self,data):

        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):

        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def predict(self, data):
        return sum(data)

#my_file = IncrementModel('test.csv')
#print(my_file.predict(my_file))