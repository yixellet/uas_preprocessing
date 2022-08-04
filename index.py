from datetime import datetime
from Passport import Passport

from Photo import Photo
from QualityControl import QualityControl
from SplitRinex import SplitRinex
from Survey import Survey
from constants import CAMERAS
from defineReliefType import defineReliefType
from survey_data import A6000_MARKS, AFS_TYPE, AREA, CAMERA_MODEL, CUSTOMER_COMPANY, FLIGHT_ALTITUDE, GROUND_PIXEL_SIZE, \
    OBJECT_NAME, PASSPORT_DIRECTORY, RELIEF_ELEVATION_RANGE, RELIEF_TYPE, RINEX, RXI_MARKS, SITE_NAME, \
    TELEMETRY, TERRITORY_TYPE
"""
objectName = input('Название объекта съёмки: ')
siteName = input('Съёмочный участок: ')
telemetryPath = input('Путь к файлу телеметрии: ')
"""
camera = CAMERAS[CAMERA_MODEL]
relief_type = defineReliefType(TERRITORY_TYPE, FLIGHT_ALTITUDE, RELIEF_ELEVATION_RANGE)
survey = Survey(TELEMETRY, relief_type, FLIGHT_ALTITUDE)
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

passport = Passport(PASSPORT_DIRECTORY, OBJECT_NAME, SITE_NAME)
passport.writeInfo(CUSTOMER_COMPANY, survey.date, survey.time['startTime'], 
    survey.time['endTime'], RELIEF_TYPE, AFS_TYPE, AREA)
passport.writeRoutes(survey.routes)

splitRINEX = SplitRinex()
splitRINEX.splitRinex(RINEX, RXI_MARKS, A6000_MARKS)