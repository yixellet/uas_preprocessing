from datetime import datetime

from constants import CAMERAS
from defineReliefType import defineReliefType
from Passport import Passport
from Photo import Photo
from QualityControl import QualityControl
from SplitRinex import SplitRinex
from Survey import Survey
from survey_data import (A6000_MARKS, AFS_TYPE, AREA, CAMERA_MODEL,
                         CONTROLER_FIO, CONTROLER_POSITION, CUSTOMER_COMPANY,
                         FLIGHT_ALTITUDE, GROUND_PIXEL_SIZE, LINE_OVERLAP,
                         OBJECT_NAME, REALIZER_FIO, REALIZER_POSITION,
                         RECEIVER, RELIEF_ELEVATION_RANGE, RELIEF_TYPE, RINEX,
                         ROUTES_ORIENTATION, RXI_MARKS, RXI_TELEMETRY,
                         SIDE_OVERLAP, SITE_NAME, TERRITORY_TYPE, UAV_MODEL)

camera = CAMERAS[CAMERA_MODEL]
relief_type = defineReliefType(TERRITORY_TYPE, FLIGHT_ALTITUDE, RELIEF_ELEVATION_RANGE)
survey = Survey(RXI_TELEMETRY, FLIGHT_ALTITUDE)
survey.extractDatetimeFromTelemetry()
groundFrameSize = survey.calcGroundFrameSize(camera)
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

# Контроль качества АФС
qualityControl = QualityControl()
qualityControl.controlAltitude(survey.photos, survey.nominalAltitude, relief_type)
qualityControl.controlAbsoluteSlopeAngles(survey.photos)
qualityControl.controlRelativeSlopeAngles(survey.routes)
qualityControl.controlOverlaps(survey.routes, survey.groundFrameSize, 80, 60, relief_type)
qualityControl.controlXmasTree(survey.routes)

# Составление паспорта АФС
passport = Passport(RXI_TELEMETRY, OBJECT_NAME, SITE_NAME)
passport.writeInfo(CUSTOMER_COMPANY, survey.date, survey.time['startTime'], 
    survey.time['endTime'], RELIEF_TYPE, AFS_TYPE, AREA, ROUTES_ORIENTATION, 
    LINE_OVERLAP, SIDE_OVERLAP, FLIGHT_ALTITUDE, GROUND_PIXEL_SIZE, camera, RECEIVER, UAV_MODEL)
passport.writeRoutes(survey.routes)
passport.closeFile((REALIZER_POSITION, REALIZER_FIO), (CONTROLER_POSITION, CONTROLER_FIO))
"""
# Разделение RINEX-файла на отдельные файлы для каждой камеры
splitRINEX = SplitRinex()
splitRINEX.splitRinex(RINEX, RXI_MARKS, A6000_MARKS)
"""
