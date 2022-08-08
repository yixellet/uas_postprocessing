import math

def calc_offsets(point, offsets):
    yaw = point['yaw'] if point['yaw'] >= 0 else 360 + point['yaw']
    dnord_y = abs(offsets['Y']) * math.cos(math.radians(yaw))
    deast_y = abs(offsets['Y']) * math.sin(math.radians(yaw))
    dnord_x = abs(offsets['X']) * math.cos(math.radians(yaw - 90 
              if offsets['X'] < 0 else yaw + 90))
    deast_x = abs(offsets['X']) * math.sin(math.radians(yaw - 90 
              if offsets['X'] < 0 else yaw + 90))
    nord = round(point['nord'] + dnord_x + dnord_y, 3)
    east = round(point['east'] + deast_x + deast_y, 3)
    elev = round(point['elevGPS'] + offsets['Z'], 3)

    return (nord, east, elev)