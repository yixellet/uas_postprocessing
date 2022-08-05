from math import degrees, atan, sqrt

def calcInverse(point1, point2):
    """
    Вычисляет расстояние и азимут направления между точками point1 и point2
    """
    dnord = point2['nord'] - point1['nord']
    deast = point2['east'] - point1['east']
    rumb = degrees(atan(abs(deast / dnord)))
    azimuth = 0
    dist = sqrt(dnord ** 2 + deast ** 2)
    
    if dnord >= 0:
        if deast > 0:
            azimuth = rumb
        elif deast < 0:
            azimuth = 360 - rumb
    elif dnord < 0:
        if deast > 0:
            azimuth = 180 - rumb
        elif deast < 0:
            azimuth = 180 + rumb
    
    return (dist, azimuth)

def calcAngleDifference(angle1: float, angle2: float):
    """Вычисляет горизонтальный угол между двумя направлениями.
    
    Принимает на вход азимуты двух направлений в десятичных градусах
    """
    difference = 0
    if (angle1 > 270 and angle2 < 90):
        difference = 360 - (angle1 - angle2)
    elif (angle1 < 90 and angle2 > 270):
        difference = 360 + (angle1 - angle2)
    else:
        difference = abs(angle1 - angle2)
    return difference