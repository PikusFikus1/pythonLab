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

def compute_daily_max_difference(time_series_list):
    day_list = []
    max_difference_list = []
    day_list = time_series_list
    day_counter = 0
    line_carry = []
    temperature_min = None
    temperature_max = None
    
    for line in day_list:
        debug = line[0]
        line[0] = (line[0]-(line[0]%86400))/86400
        if len(line_carry) == 0 or line_carry[0] != line[0]:
            if len(line_carry) != 0:
                max_difference_list.append([day_counter,debug,temperature_max,temperature_min,temperature_max-temperature_min])
                temperature_max = None
            line_carry = line
            day_counter += 1
            if temperature_max == None:
                temperature_max = line[1]
                temperature_min = line[1]
        else:
            if temperature_max < line[1]:
                temperature_max = line[1]
            if temperature_min > line[1]:
                temperature_min = line[1]
            
        line.append(day_counter)
    max_difference_list.append([day_counter,debug,temperature_max,temperature_min,temperature_max-temperature_min])        
    return (max_difference_list)
    


time_series_file = CSVTimeSeriesFile(name='data_with_trash.csv')

time_series = time_series_file.get_data()

our_list = compute_daily_max_difference(time_series)

for item in our_list:
    print(item)