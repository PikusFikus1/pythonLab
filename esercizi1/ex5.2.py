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
            if len(elements[0])!=0 or len(elements[1])!=0:
                if elements[0]!="Date":
                    myList.append(elements)
        return myList




class NumericalCSVFile(CSVFile):
    
    def convToFloat(self):
        data = super().get_data();
        num_data = []

        for row_data in data:
            num_row = []

            for i,element in enumerate(row_data):
                if i==0:
                    num_row.append(element)
                else:
                    try:
                        num_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
            if len(num_row) == len(data):
                num_data.append(num_row)
                        
        return num_data

#myList = NumericalCSVFile('shampoo_sales.csv')
#print(myList.convToFloat())