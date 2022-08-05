from calc_offsets import calc_offsets
from centersToArray import centersToArray
from config import RX1
from splitByRoutes import splitByRoutes

centers_path = 'E:\\ГЕОДЕЗИЯ\\АЭРОФОТОСЪЕМКА\\Селитренное_2022\\010822\\avp1\\Селитренное_010822_центры_МСК30-1_1.txt'
telemetry_path = 'A:\\AFS_2022\\Селитренное\\1\\photo\\rgb\\2022_08_01_SonyRX1RM2_g201b20445_f001_telemetry.txt'

centers = centersToArray(centers_path, ';', ['name', 'nord', 'east', 'elev', 'time', 'rmsxy', 'rmsh'], 0)
telemetry = centersToArray(telemetry_path, '\t', ['name', 'nord', 'east', 'elevBaro', 'roll', 'pitch', 'yaw', 'time', 'elevGPS'], 6)

routes = splitByRoutes(centers)
print(routes)


"""
with open('photo_centers_RX1.txt', 'r') as source, open('photo_centers_RX1_offsets.txt', 'w') as result:
    
    points = []
    for line in source:
        line_array = line.split(';')
        point = {}
        point['name'] = int(line_array[0])
        point['nord'] = float(line_array[1].replace(',', '.'))
        point['east'] = float(line_array[2].replace(',', '.'))
        point['elev'] = float(line_array[3].replace(',', '.'))
        point['time'] = line_array[4]
        point['stdne'] = float(line_array[7].replace(',', '.'))
        point['stdh'] = float(line_array[8].replace(',', '.'))
        points.append(point)
    
    for i in range(len(points) - 1):
        cur_point = points[i]
        next_point = points[i + 1]
        points[i]['azimuth'] = calc_azimuth(cur_point, next_point)
    
    points[-1]['azimuth'] = calc_azimuth(points[-2], points[-1])

    for i in range(len(points) - 2):
        cur_point = points[i]
        next_point = points[i + 1]
        next2_point = points[i + 2]
        dazimuth = next2_point['azimuth'] - next_point['azimuth']
        if abs(dazimuth) >= 15:
            next_point['azimuth'] = cur_point['azimuth']

    for point in points:
        p = calc_offsets(point, RX1['X'], RX1['Y'], RX1['Z'])
        result.write(str(p['name']) + '\t' + str(p['nord']) + '\t' + str(p['east']) + '\t' + str(p['elev']) + '\t' + str(p['stdn']) + '\t' + str(p['stde']) + '\t' + str(p['stdh']) + '\n')
    
"""