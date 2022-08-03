from datetime import datetime
from Camera import Camera
from Passport import Passport

from Photo import Photo
from QualityControl import QualityControl
from Survey import Survey
"""
objectName = input('Название объекта съёмки: ')
siteName = input('Съёмочный участок: ')
telemetryPath = input('Путь к файлу телеметрии: ')
"""
rx1cam = Camera(35, 0.0045, 7952, 5304, 71.6, 'RGB')
#a6000cam = Camera(20, 0.0039, 6000, 4000, 70.7, 'NIR')
survey = Survey('Протока Николаевская', '1')
survey.extractDatetimeFromTelemetry()
groundFrameSize = survey.calcGroundFrameSize()
photoPointsRawArray = survey.createPhotoPointsArray()

for point in photoPointsRawArray:
    dateTimeArray = point[7].split(' ')
    dateArray = dateTimeArray[0].split('.')
    timeArray = dateTimeArray[1].split(':')
    secondsArray = timeArray[2].split('.')
    survey.addPhotos(Photo(point[0],
                           float(point[1]),
                           float(point[2]),
                           float(point[3]),
                           float(point[8][:-1]),
                           float(point[4]),
                           float(point[5]),
                           float(point[6]),
                           datetime(int(dateArray[0]), int(dateArray[1]), int(dateArray[2]), 
                           int(timeArray[0]), int(timeArray[1]), int(secondsArray[0]), int(secondsArray[1]))
    ))

survey.splitByRoutes()
qualityControl = QualityControl()
qualityControl.controlAltitude(survey.photos, survey.nominalAltitude, 'HILLS')
qualityControl.controlAbsoluteSlopeAngles(survey.photos)
qualityControl.controlRelativeSlopeAngles(survey.routes)
qualityControl.controlOverlaps(survey.routes, 80, 60, 'NATURE', 'HILLS')

passport = Passport('test', survey.objectName, survey.siteName)
passport.writeInfo('Служба природопользования', survey.date, survey.time['startTime'], survey.time['endTime'])
passport.writeRoutes(survey.routes)