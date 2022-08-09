from pyproj import CRS, Transformer

def transformCoord(nord, east, crsFrom, crsTo):
    msk1str = '+proj=tmerc +lat_0=0 +lon_0=46.05 +k=1 +x_0=1300000 +y_0=-4714743.504 +ellps=krass +towgs84=23.57,-140.95,-79.8,0,0.35,0.79,-0.22 +units=m +no_defs'
    msk2str = '+proj=tmerc +lat_0=0 +lon_0=49.05 +k=1 +x_0=2300000 +y_0=-4714743.504 +ellps=krass +towgs84=23.57,-140.95,-79.8,0,0.35,0.79,-0.22 +units=m +no_defs'

    crs_list = {
        'МСК-30 (зона 1)': CRS.from_proj4(msk1str),
        'МСК-30 (зона 2)': CRS.from_proj4(msk2str),
        'UTM (зона 38)': CRS.from_epsg(32638),
        'UTM (зона 39)': CRS.from_epsg(32639),
    }
    transformer = None
    if crsFrom == 'МСК-30 (зона 1)' or crsFrom == 'МСК-30 (зона 2)':
        transformer = Transformer.from_proj(crs_list[crsFrom], crs_list[crsTo])
    elif crsFrom == 'UTM (зона 38)' or crsFrom == 'UTM (зона 39)':
        transformer = Transformer.from_crs(crs_list[crsFrom], crs_list[crsTo])
    
    result = transformer.transform(nord, east)
    return result