from angleCalc import calcAngleDifference, calcAzimuth
from constants import (ADMISSIBLE_ELEV_DEVIATIONS, CRITICAL_ABSOLUTE_ANGLE,
                       CRITICAL_OVERLAPS, CRITICAL_RELATIVE_ANGLE,
                       NOMINAL_OVERLAPS, STRAIGHT_LINE_RESIDUALS, XMAS_TREE)


class QualityControl(object):
    """
    Класс, содержащий методы для контроля качества
    """
    altControl = {
        'meanAlt': None,
        'photos': [],
        'outOfTolerance': None
    }
    absSlopeControl = {
        'nominalRollAngle': 0,
        'nominalPitchAngle': 0,
        'photos': [],
        'outOfTolerance': None
    }
    relSlopeControl = {
        'photoPairs': [],
        'outOfTolerance': None
    }
    lineOverlapsControl = {
        'tolerance': None,
        'photoPairs': [],
        'outOfTolerance': None
    }
    sideOverlapsControl = {
        'tolerance': None,
        'routePairs': [],
        'outOfTolerance': None
    }
    xmasTreeControl = {
        'tolerance': None,
        'photos': [],
        'outOfTolerance': None
    }
    straightnessControl = {
        'tolerance': STRAIGHT_LINE_RESIDUALS,
        'photos': [],
        'outOfTolerance': None
    }

    def controlAltitude(self, photos, nominalAltitude: int, 
                        relief_type: str):
        """Вычисляет отклонения от средней высоты полета в метрах и в процентах"""
        altSum = 0
        out_of_tolerance_count = 0
        elev_tolerance = ADMISSIBLE_ELEV_DEVIATIONS[relief_type]
        for photo in photos:
            altSum += photo.altGPS
        self.altControl['meanAlt'] = altSum / len(photos)
        for photo in photos:
            residual = round(photo.altGPS - self.altControl['meanAlt'], 1)
            percentResidual = round(residual / nominalAltitude * 100, 1)
            self.altControl['photos'].append({
                'name': photo.name,
                'altResidual': residual,
                'altResidualPercent': percentResidual,
                'ok': True if percentResidual <= elev_tolerance else False
            })
            if abs(percentResidual) > elev_tolerance:
                out_of_tolerance_count += 1
        self.altControl['outOfTolerance'] = (out_of_tolerance_count, out_of_tolerance_count/len(photos)*100)
        return self.altControl

    def controlAbsoluteSlopeAngles(self, photos):
        """Вычисляет отклонения абсолютных углов наклона (крен и тангаж)
        в градусах"""
        out_of_tolerance_count = 0
        for photo in photos:
            rollResidual = photo.roll - self.absSlopeControl['nominalRollAngle']
            pitchResidual = photo.pitch - self.absSlopeControl['nominalPitchAngle']
            rollOk = abs(rollResidual) <= CRITICAL_ABSOLUTE_ANGLE
            pitchOk = abs(pitchResidual) <= CRITICAL_ABSOLUTE_ANGLE
            self.absSlopeControl['photos'].append({
                'name': photo.name,
                'rollResidual': rollResidual,
                'pitchResidual': pitchResidual,
                'rollOk': rollOk,
                'pitchOk': pitchOk
            })
            if not rollOk or not pitchOk:
                out_of_tolerance_count += 1
        self.absSlopeControl['outOfTolerance'] = (out_of_tolerance_count, out_of_tolerance_count/len(photos)*100)
        return self.absSlopeControl
    
    def controlRelativeSlopeAngles(self, routes):
        """Вычисляет отклонения взаимных углов наклона в градусах"""
        out_of_tolerance_count = 0
        pairCount = 0
        for route in routes:
            for i in range(0, len(route['photos']) - 2):
                relativeRollAngle = abs(route['photos'][i].roll - route['photos'][i+1].roll)
                relativePitchAngle = abs(route['photos'][i].pitch - route['photos'][i+1].pitch)
                rollOk = relativeRollAngle <= CRITICAL_RELATIVE_ANGLE
                pitchOk = relativePitchAngle <= CRITICAL_RELATIVE_ANGLE
                self.relSlopeControl['photoPairs'].append({
                    'leftPhotoName': route['photos'][i].name,
                    'rightPhotoName': route['photos'][i+1].name,
                    'relativeRollAngle': relativeRollAngle,
                    'relativePitchAngle': relativePitchAngle,
                    'rollOk': rollOk,
                    'pitchOk': pitchOk
                })
                if not rollOk or not pitchOk:
                    out_of_tolerance_count += 1
                pairCount += 1
        self.relSlopeControl['outOfTolerance'] = (out_of_tolerance_count, 
                                        out_of_tolerance_count/pairCount*100)
        return self.relSlopeControl

    def controlOverlaps(self, routes, groundFrameSize, lineOverlap: int, sideOverlap: int, reliefType: int):
        """Вычисляет отклонения от номинальных значений продольного
        и поперечного перекрытий
        """
        nominalLineOverlap = NOMINAL_OVERLAPS[reliefType]['LINE']
        nominalSideOverlap = NOMINAL_OVERLAPS[reliefType]['SIDE']
        lineCoef = nominalLineOverlap / lineOverlap
        sideCoef = nominalSideOverlap / sideOverlap
        relief_type_number = None
        if reliefType == 1 or reliefType == 4:
            relief_type_number = 1
        elif reliefType == 2 or reliefType == 5 or reliefType == 6:
            relief_type_number = 2
        else:
            relief_type_number = 3
        lineTolerance = (nominalLineOverlap + CRITICAL_OVERLAPS[relief_type_number]['LINE']['MIN'] * lineCoef, 
                         nominalLineOverlap + CRITICAL_OVERLAPS[relief_type_number]['LINE']['MAX'] * lineCoef + 7)
        sideTolerance = [nominalSideOverlap + CRITICAL_OVERLAPS[relief_type_number]['SIDE']['MIN'] * sideCoef, 
                         nominalSideOverlap + CRITICAL_OVERLAPS[relief_type_number]['SIDE']['MAX'] * sideCoef + 7]
        out_of_tolerance_count = 0
        pairCount = 0
        for route in routes:
            for i in range(len(route['photos']) - 2):
                distBetweenPhotoCenters = calcAzimuth(route['photos'][i].lat, 
                                                      route['photos'][i].lon, 
                                                      route['photos'][i+1].lat, 
                                                      route['photos'][i+1].lon)[0]
                overlap = (groundFrameSize[1] - distBetweenPhotoCenters) / groundFrameSize[1] * 100
                lineOverlapOk = overlap >= lineTolerance[0] and overlap <= lineTolerance[1]
                self.lineOverlapsControl['photoPairs'].append(
                    {
                        'leftPhotoName': route['photos'][i].name,
                        'rightPhotoName': route['photos'][i+1].name,
                        'lineOverlap': overlap,
                        'ok': lineOverlapOk
                    }
                )
                if not lineOverlapOk:
                    out_of_tolerance_count += 1
                pairCount += 1
        self.lineOverlapsControl['tolerance'] = lineTolerance
        self.lineOverlapsControl['outOfTolerance'] = (out_of_tolerance_count, 
                                        out_of_tolerance_count/pairCount*100)
        
        out_of_tolerance_count = 0
        pairCount = 0
        for i in range(len(routes) - 2):
            distAtStart = 0

        return self.lineOverlapsControl

    def controlXmasTree(self, routes):
        out_of_tolerance_count = 0
        photo_count = 0
        for route in routes:
            for photo in route['photos']:
                yaw = photo.yaw if photo.yaw > 0 else 360 + photo.yaw
                xtree = calcAngleDifference(yaw, route['azimuth'][1])
                ok = xtree <= XMAS_TREE
                self.xmasTreeControl['photos'].append({
                    'name': photo.name,
                    'xtree': xtree,
                    'ok': ok
                })
                if not ok:
                    out_of_tolerance_count += 1
                photo_count += 1
        self.xmasTreeControl['tolerance'] = XMAS_TREE
        self.xmasTreeControl['outOfTolerance'] = (out_of_tolerance_count, out_of_tolerance_count/photo_count*100)
        return self.xmasTreeControl
    
    def controlStraightness(self, routes):
        out_of_tolerance_count = 0
        photo_count = 0
        for route in routes:
            for photo in route['photos']:
                yaw = photo.yaw if photo.yaw > 0 else 360 + photo.yaw
                xtree = calcAngleDifference(yaw, route['azimuth'][1])
                ok = xtree <= XMAS_TREE
                self.straightnessControl['photos'].append({
                    'name': photo.name,
                    'xtree': xtree,
                    'ok': ok
                })
                if not ok:
                    out_of_tolerance_count += 1
                photo_count += 1
        self.straightnessControl['outOfTolerance'] = (out_of_tolerance_count, out_of_tolerance_count/photo_count*100)
        return self.straightnessControl
