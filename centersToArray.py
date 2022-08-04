def centersToArray(file, delimiter: str, structure):
    """Конвертирует файл в список словарей"""
    with open(file, 'r') as catalogue:
        points = []
        for line in catalogue:
            print(line)
            line_array = line.split(delimiter)
            point = {}
            for element in range(len(structure) - 1):
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
    ar = centersToArray('photo_centers_RX1.txt', 
        ';', 
        ['name', 'nord', 'east', 'elev', 'time', 'empty', 'empty', 'rmsxy', 'rmsh'])
    #print(ar)