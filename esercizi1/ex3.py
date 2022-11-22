class CSVFile():

    def __inti__(self, name):
        self.name = name
        
    def get_data(self):
        myList = []
        my_file = open(format(self.name), 'r')
        
        for line in my_file:
            elements = line.split(',')
            myList.append(elements)
        return myList

