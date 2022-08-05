from angleCalc import calcAngleDifference, calcInverse

def splitByRoutes(points):
    routes = []
    route = {
        'photos': [],
        'azimuth': None
    }
    count = 1
    route['photos'].append(points[count-1])
    route['photos'].append(points[count])
    while count <= len(points) - 2:
        basis0 = calcInverse(points[count-1], points[count])
        basis1 = calcInverse(points[count], points[count+1])
        yaw = points[count+1]['yaw'] if points[count+1]['yaw'] > 0 else 360 + points[count+1]['yaw']
        deltaAzimuth = calcAngleDifference(basis0[1], basis1[1])
        deltaAzimuthAndYaw = calcAngleDifference(basis0[1], yaw)
        if deltaAzimuth <= 10 and deltaAzimuthAndYaw <= 10 and abs(basis0[0] - basis1[0]) <= 10:
            route['photos'].append(points[count+1])
            count += 1
        else:
            route['azimuth'] = calcInverse(route['photos'][0], route['photos'][-1])
            routes.append(route)
            route = {
                'photos': [],
                'azimuth': None
            }
            count += 2
            route['photos'].append(points[count-1])
            route['photos'].append(points[count])
    
    route['azimuth'] = calcInverse(route['photos'][0], route['photos'][-1])
    routes.append(route)

    return routes