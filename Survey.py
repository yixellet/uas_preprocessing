from datetime import date, time
import re

from angleCalc import calcAngleDifference, calcAzimuth

class Survey(object):
    """Объект АФС"""
    date = None
    time = {}
    photos = []
    routes = []
    groundFrameSize = None

    def __init__(self, 
                 objectName: str = '<название объекта>', 
                 siteName: str = '<съёмочный участок>',
                 telemetryPath: str = '/home/owgrant/Документы/Работа/' \
                 'Данные_для_тестирования_плагинов_QGIS/' \
                 '2022_04_21_SonyRX1RM2_g201b20445_f001_telemetry.txt',
                 reliefType: str = 'HILLS',
                 nominalAltitude: int = 300,
                 groungPixelSize: float = 0.04) -> None:

        self.objectName = objectName
        self.siteName = siteName
        self.telemetryPath = telemetryPath
        self.reliefType = reliefType
        self.nominalAltitude = nominalAltitude
        self.groungPixelSize = groungPixelSize
    
    def __str__(self) -> str:
        return '\tАЭРОФОТОСЪЁМКА\nОбъект:\t\t\t{}\nСъёмочный участок:\t{}' \
        '\nДата:\t\t\t{}\nВремя начала:\t\t{}\nВремя окончания:\t{}' \
        '\nКоличество снимков:\t{}'.format(self.objectName, self.siteName, 
        self.date, self.time['startTime'], self.time['endTime'], len(self.photos))
    
    def extractDatetimeFromTelemetry(self) -> None:
        with open(self.telemetryPath, 'r') as file:
            dateTimeLine = file.readline()
            dateString = re.search(r'\d{4}.\d{2}.\d{2}', dateTimeLine).group().split('.')
            self.date = date(int(dateString[0]), 
                                      int(dateString[1]), 
                                      int(dateString[2])
            )
            timeArray = re.findall(r'\d{2}:\d{2}:\d{2}', dateTimeLine)
            self.time['startTime'] = time(int(timeArray[0].split(':')[0]), 
                                                   int(timeArray[0].split(':')[1]), 
                                                   int(timeArray[0].split(':')[2])
            )
            self.time['endTime'] = time(int(timeArray[1].split(':')[0]), 
                                                 int(timeArray[1].split(':')[1]), 
                                                 int(timeArray[1].split(':')[2])
            )
    
    def createPhotoPointsArray(self):
        with open(self.telemetryPath, 'r') as file:
            telemetry_array = []
            for line in file.readlines()[6:]:
                telemetry_array.append(line.split('\t'))
        return telemetry_array
    
    def addPhotos(self, photo: object) -> None:
        self.photos.append(photo)

    def splitByRoutes(self):
        route = {
            'photos': [],
            'azimuth': None
        }
        count = 1
        route['photos'].append(self.photos[count-1])
        route['photos'].append(self.photos[count])
        while count <= len(self.photos) - 2:
            name = self.photos[count].name
            basis0 = calcAzimuth(self.photos[count-1].lat, self.photos[count-1].lon, 
                              self.photos[count].lat, self.photos[count].lon)
            basis1 = calcAzimuth(self.photos[count].lat, self.photos[count].lon, 
                              self.photos[count+1].lat, self.photos[count+1].lon)
            yaw = self.photos[count+1].yaw if self.photos[count+1].yaw > 0 else 360 + self.photos[count+1].yaw
            deltaAzimuth = calcAngleDifference(basis0[1], basis1[1])
            deltaAzimuthAndYaw = calcAngleDifference(basis0[1], yaw)
            if deltaAzimuth <= 10 and deltaAzimuthAndYaw <= 10 and abs(basis0[0] - basis1[0]) <= 10:
                route['photos'].append(self.photos[count+1])
                count += 1
            else:
                route['azimuth'] = calcAzimuth(route['photos'][0].lat, 
                                               route['photos'][0].lon, 
                                               route['photos'][-1].lat, 
                                               route['photos'][-1].lon,)
                self.routes.append(route)
                route = {
                    'photos': [],
                    'azimuth': None
                }
                count += 2
                route['photos'].append(self.photos[count-1])
                route['photos'].append(self.photos[count])
        
        route['azimuth'] = calcAzimuth(route['photos'][0].lat, 
                                        route['photos'][0].lon, 
                                        route['photos'][-1].lat, 
                                        route['photos'][-1].lon,)
        self.routes.append(route)

    def calcGroundFrameSize(self):
        if self.nominalAltitude == 300:
            groundFrameWidth = 270
            groundFrameHeight = 180
        self.groundFrameSize = (groundFrameWidth, groundFrameHeight)
        return self.groundFrameSize