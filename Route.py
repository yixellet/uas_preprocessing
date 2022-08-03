import math

class Route(object):
    photos = []
    azimuth = None

    def addPhoto(self, photo: object) -> str:
        self.photos.append(photo)
        return photo.name
    
    def calcAzimuth(self, startPoint, endPoint) -> float:
        # радиус сферы (Земли)
        rad = 6372795

        #в радианах
        lat1 = startPoint.lat * math.pi / 180.
        lat2 = endPoint.lat * math.pi / 180.
        long1 = startPoint.lon * math.pi / 180.
        long2 = endPoint.lon * math.pi / 180.

        #косинусы и синусы широт и разницы долгот
        cl1 = math.cos(lat1)
        cl2 = math.cos(lat2)
        sl1 = math.sin(lat1)
        sl2 = math.sin(lat2)
        delta = long2 - long1
        cdelta = math.cos(delta)
        sdelta = math.sin(delta)

        #вычисления длины большого круга
        y = math.sqrt(math.pow(cl2 * sdelta, 2) + math.pow(cl1 * sl2 - sl1 * cl2 * cdelta, 2))
        x = sl1 * sl2 + cl1 * cl2 * cdelta
        ad = math.atan2(y, x)
        dist = ad * rad

        #вычисление начального азимута
        x = (cl1 * sl2) - (sl1 * cl2 * cdelta)
        y = sdelta * cl2
        z = math.degrees(math.atan(-y / x))

        if (x < 0):
            z = z + 180.

        z2 = (z + 180.) % 360. - 180.
        z2 = - math.radians(z2)
        anglerad2 = z2 - ((2 * math.pi) * math.floor((z2 / (2 * math.pi))))
        angledeg = (anglerad2 * 180.) / math.pi

        self.azimuth = angledeg

        return angledeg
