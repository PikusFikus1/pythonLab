def sum_list():
    values = []
    tot = 0

    my_file = open('ex2file.csv', 'r')
    for line in my_file:

        elements = line.split(',')

        if elements[0] != 'Date':
            date = elements[0]
            value = elements[1]
            tot += float(value)
            print(tot)
    return tot