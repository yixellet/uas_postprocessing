from datetime import datetime, timedelta

def normalizeDatetime(string):
    normalized = datetime(int(string[:4]), 
                                     int(string[5:7]), 
                                     int(string[8:10]), 
                                     int(string[11:13]), 
                                     int(string[14:16]), 
                                     int(string[17:19]), 
                                     int(string[20:]))
    return normalized

def interpolation(prevPoint, nextPoint, currentTime):
    currentPoint = ()
    currentTimeNormal = normalizeDatetime(currentTime)
    prevTimeNormal = normalizeDatetime(prevPoint['time'])
    nextTimeNormal = normalizeDatetime(nextPoint['time'])
    deltaNordCommon = prevPoint['nord'] - nextPoint['nord']
    deltaEastCommon = prevPoint['east'] - nextPoint['east']
    deltaTimeCommon = timedelta(prevTimeNormal, nextTimeNormal)
    deltaTimePrev = timedelta(prevTimeNormal, currentTimeNormal)
    deltaNordPrev = deltaTimePrev * deltaNordCommon / deltaTimeCommon
    deltaEastPrev = deltaTimePrev * deltaEastCommon / deltaTimeCommon

    return currentPoint