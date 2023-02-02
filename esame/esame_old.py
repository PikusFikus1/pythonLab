class CSVTimeSeriesFile():

    def __init__(self,name):
        self.name = name

    def get_data(self):
        my_list = []
        my_file = open(format(self.name), 'r')

        for line in my_file:
            line = line.strip()
            line = line.split(',')
            if(line[0] != 'epoch'):
                line[0] = int(line[0])
                line[1] = float(line[1])
                my_list.append(line)
        
        return(my_list)

class ExamException(Exception):
    pass

def compute_daily_max_difference(time_series_list):
    max_difference_list = []
    line_carry = []
    temperature_min = None
    temperature_max = None
    daily_mesaurment_flag = False
    
    for line in time_series_list:
        line[0] = (line[0]-(line[0]%86400))/86400
        if len(line_carry) == 0 or line_carry[0] != line[0]:
            if len(line_carry) != 0:
                if daily_mesaurment_flag == False:
                    max_difference_list.append(None)
                else:
                    max_difference_list.append(temperature_max-temperature_min)
                    daily_mesaurment_flag = False
                temperature_max = None
            line_carry = line
            if temperature_max == None:
                temperature_max = line[1]
                temperature_min = line[1]
        else:
            if temperature_max < line[1]:
                temperature_max = line[1]
            if temperature_min > line[1]:
                temperature_min = line[1]
            daily_mesaurment_flag = True
    if daily_mesaurment_flag == False:
        max_difference_list.append(None)
    else:
        max_difference_list.append(temperature_max-temperature_min)        
    return (max_difference_list)
    


time_series_file = CSVTimeSeriesFile(name='data_with_trash.csv')

time_series = time_series_file.get_data()

our_list = compute_daily_max_difference(time_series)

for i,item in enumerate(our_list):
    print([i,item])