class CSVFile():

    def __init__(self, name):
        self.name = name
        
    def get_data(self):
        myList = []
        my_file = open(format(self.name), 'r')
        
        for line in my_file:
            elements = line.split(',')
            elements[1] = elements[1].strip('\n')
            myList.append(elements)
            myList
        return myList