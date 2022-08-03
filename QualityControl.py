from constants import ADMISSIBLE_ELEV_DEVIATIONS, CRITICAL_ABSOLUTE_ANGLE, CRITICAL_OVERLAPS, CRITICAL_RELATIVE_ANGLE, NOMINAL_OVERLAPS

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

    def controlAltitude(self, photos, nominalAltitude: int, 
                        relief_type: str = "FLATLAND"):
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
                ph0 = route['photos'][i].name
                ph1 = route['photos'][i+1].name
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
        self.relSlopeControl['outOfTolerance'] = (out_of_tolerance_count, out_of_tolerance_count/pairCount*100)
        return self.relSlopeControl

    def controlOverlaps(self, routes, lineOverlap: int, sideOverlap: int, 
                        territoryType: str, reliefType: str):
        """Вычисляет отклонения от номинальных значений продольного
        и поперечного перекрытий
        """
        nominalLineOverlap = NOMINAL_OVERLAPS[territoryType][reliefType]['LINE']
        nominalSideOverlap = NOMINAL_OVERLAPS[territoryType][reliefType]['SIDE']
        lineCoef = nominalLineOverlap / lineOverlap
        sideCoef = nominalSideOverlap / sideOverlap
        lineTolerance = [CRITICAL_OVERLAPS[reliefType]['LINE']['MIN'] * lineCoef, 
                         CRITICAL_OVERLAPS[reliefType]['LINE']['MAX'] * lineCoef + 7]
        sideTolerance = [CRITICAL_OVERLAPS[reliefType]['SIDE']['MIN'] * sideCoef, 
                         CRITICAL_OVERLAPS[reliefType]['SIDE']['MAX'] * sideCoef + 7]
        for route in routes:
            for i in range(0, len(route['photos']) - 2):
                pass
