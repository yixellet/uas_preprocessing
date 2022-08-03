from datetime import datetime

class Photo(object):
    """Объект фотоснимка"""
    def __init__(self, 
                 name: str, 
                 lat: float, 
                 lon: float, 
                 altBaro: float,
                 altGPS: float,
                 roll: float,
                 pitch: float,
                 yaw: float,
                 dateTime: datetime) -> None:
        self.name = name
        self.lat = lat
        self.lon = lon
        self.altBaro = altBaro
        self.altGPS = altGPS
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.dateTime = dateTime
    
    def __str__(self):
        return '\tСНИМОК\nИмя:\t\t\t{}\nШирота:\t\t\t{}\nДолгота:\t\t{}\n' \
        'Высота барометрическая:\t{}\nВысота ГНСС:\t\t{}' \
        '\nКрен:\t\t\t{}\nТангаж:\t\t\t{}\nРысканье:\t\t{}'\
        '\nДата и время:\t\t{}'.format(self.name, self.lat, 
        self.lon, self.altBaro, self.altGPS, self.roll, self.pitch, 
        self.yaw, self.dateTime)