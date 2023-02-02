class CSVFile():

    def __init__(self, name):
        self.name = name
        
    def get_data(self):
        myList = []
        try:
            my_file = open(format(self.name), 'r')
        except:
            print('Errore: file non esistente')
        
        for line in my_file:
            elements = line.strip()
            elements = elements.split(',')
            if len(elements[0])!=0 and len(elements[1])!=0:
                if elements[0]!="Date":
                    myList.append(elements)
        return myList

