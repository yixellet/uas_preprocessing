CRITICAL_RELATIVE_ANGLE = 6.0
CRITICAL_ABSOLUTE_ANGLE = 13.0
ADMISSIBLE_ELEV_DEVIATIONS = {
    1: 3,
    2: 5,
    3: 5
}
NOMINAL_OVERLAPS = {
    1: {
        "LINE": 63,
        "SIDE": 32
    },
    2: {
        "LINE": 67,
        "SIDE": 35
    },
    3: {
        "LINE": 72,
        "SIDE": 40
    },
    4: {
        "LINE": 76,
        "SIDE": 60
    },
    5: {
        "LINE": 77,
        "SIDE": 62
    },
    6: {
        "LINE": 79,
        "SIDE": 64
    },
    7: {
        "LINE": 81,
        "SIDE": 67
    },
    8: {
        "LINE": 82,
        "SIDE": 70
    }
}
CRITICAL_OVERLAPS = {
    1: {
        "LINE": {
            "MIN": -7,
            "MAX": 6
        },
        "SIDE": {
            "MIN": -12,
            "MAX": 10
        }
    },
    2: {
        "LINE": {
            "MIN": -9,
            "MAX": 7
        },
        "SIDE": {
            "MIN": -15,
            "MAX": 12
        }
    },
    3: {
        "LINE": {
            "MIN": -12,
            "MAX": 8
        },
        "SIDE": {
            "MIN": -19,
            "MAX": 13
        }
    }
}
XMAS_TREE = 14
STRAIGHT_LINE_RESIDUALS = 3
UAV_MODEL = 'Геоскан 201 Агрогеодезия'
CAMERAS = {
    1: {
        'NAME': 'Sony RXI RMII',
        'SERIAL_NUMBER': 7160289,
        'FOCAL_LENGTH': 30,
        'LENS_ANGLE': 64,
        'FRAME_SIZE': (7952, 5304),
        'PIXEL_SIZE': 0.0045,
        'SPECTRUM_SIGNATURE': 'RGB',
        'FILE_FORMAT': 'JPEG',
        'COORD_SYS': 'Вправо'
    },
    2: {
        'NAME': 'Sony A6000',
        'SERIAL_NUMBER': 7391829,
        'FOCAL_LENGTH': 20,
        'LENS_ANGLE': 68,
        'FRAME_SIZE': (6000, 4000),
        'PIXEL_SIZE': 0.0039,
        'SPECTRUM_SIGNATURE': 'NIR',
        'FILE_FORMAT': 'ARW',
        'COORD_SYS': 'Вправо'
    }
}
AFS_TYPES = {
    1: 'Площадная надирная',
    2: 'Линейная надирная',
    4: 'Площадная перспективная',
    4: 'Линейная перспективная'
}