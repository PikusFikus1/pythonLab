#file_name = 'shampoo_sales.csv'

def sum_csv(file_name):
    values = []

    fileVal = open(file_name, 'r')
    for line in fileVal:
        row = line.split(',')
        if row[0] != 'Date':
            row[1].strip('\n')
            try:
                values.append(float(row[1]))
            except:
                pass
    if values == []:
        return None
    return sum(values)

#print(sum_csv(file_name))

