def sum_csv(file_name):
    values = []
    tot = 0

    my_file = open(file_name, 'r')
    for line in my_file:

        elements = line.split(',')

        if elements[0] != 'Date':
            value = elements[1]
            values.append(float(value))
    return sum(values)

