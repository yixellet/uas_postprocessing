def centersToArray(file, delimiter: str, structure, startWith: int):
    """Конвертирует файл в список словарей"""
    with open(file, 'r') as catalogue:
        points = []
        for line in catalogue.readlines()[startWith:]:
            line_array = line.split(delimiter)
            point = {}
            for element in range(len(structure)):
                toAppend = None
                if structure[element] == 'name' or structure[element] == 'time':
                    toAppend = line_array[element]
                else:
                    toAppend = float(line_array[element].replace(',', '.'))
                if structure[element] != 'empty':
                    point[structure[element]] = toAppend
            points.append(point)
    return points

if __name__ == '__main__':
    ar = centersToArray('E:\\ГЕОДЕЗИЯ\\АЭРОФОТОСЪЕМКА\\Селитренное_2022\\010822\\avp1\\Селитренное_010822_центры_МСК30-1_1.txt', 
        ';', 
        ['name', 'nord', 'east', 'elev', 'time', 'rmsxy', 'rmsh'])
    print(ar)