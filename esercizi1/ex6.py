class CSVFile():

    def __init__(self, name):
        self.name = name
        if type(self.name) is not str:
            raise Exception('Errore, parametro: "{}"'.format(self.name))
        
    def get_data(self, start=None, end=None):
        myList = []
        try:
            my_file = open(format(self.name), 'r')
        except:
            print('Errore: file non esistente')
        if start!=None and start <= 0:
            raise Exception('Errore, parametro "{}"'.format(start))
        for i,line in enumerate(my_file):
            elements = line.strip()
            elements = elements.split(',')
            
            if len(elements[0])!=0 and len(elements[1])!=0:
                if (elements[0]!="Date" and (start==None or i>=start-1) and (end==None or i<=end-1)):
                    myList.append(elements)
                    
        return myList

