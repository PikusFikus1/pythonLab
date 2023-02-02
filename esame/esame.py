class CSVTimeSeriesFile():

    def __init__(self,name = None):
        self.name = name

    def get_data(self):
        my_list = []
        control_list = []
        if self.name == None:          #controlla se è stato inserito un nome di qualche file
            raise ExamException('Nome file non inserito')
        try:                            #prova ad aprire il file, in caso contrario alza un'eccezione
            my_file = open(format(self.name), 'r')
        except:
            raise ExamException('Nome file non valido')
        try:                            #controlla se il file è leggibile
            my_file.readline()
        except:
            raise ExamException('File non supportato')
        
        previous_line = None

        for i,line in enumerate(my_file):
            line = line.strip()
            line = line.split(',')
            if(line[0] != 'epoch'):
                try:                #prova a convertire i dati in int e float, in caso contrario ignora la riga
                    line[0] = int(line[0])
                    line[1] = float(line[1])
                except:
                    pass
                else:               
                    if previous_line != None and line[0] < previous_line:    #controlla se: è gia stata salvata una previous_line e se line[0] e previous_line non sono ordinate
                        raise ExamException('La lista non è ordinata')
                    my_list.append(line)
                    control_list.append(line[0])
                    previous_line = line[0]
                    if len(set(control_list)) != len(control_list):    #controlla, se l'epoch è unico
                        raise ExamException('Epoch duplicati non supportati')
        my_file.close()
        return(my_list)

class ExamException(Exception):
    pass

def compute_daily_max_difference(time_series_list):
    max_difference_list = []
    line_carry = []
    daily_list = []

    if len(time_series_list) == 0:    #controlla se la lista in entrata è vuota
        raise ExamException('Lista vuota')
    
    def append_selector():        #controlola se il giorno ha una o piu misurazioni
        if len(daily_list) == 1: max_difference_list.append(None)
        else: max_difference_list.append(max(daily_list)-min(daily_list))

    for i,line in enumerate(time_series_list):
        line[0] = line[0]-(line[0]%86400)
        if i != 0 and line[0] != line_carry[0]:    #controlla se l'elemento non è il primo del for e se i giorni sono diversi
            append_selector()
            daily_list.clear()
        daily_list.append(line[1])    #riempie una lista con solamente misurazioni dello stesso giorno
        line_carry = line
    append_selector()    #differenza massima dell'ultimo giorno
        
    return (max_difference_list)
    

time_series_file = CSVTimeSeriesFile(name='data.csv')

time_series = time_series_file.get_data()

our_list = compute_daily_max_difference(time_series)

for i,item in enumerate(our_list):
    print(item)