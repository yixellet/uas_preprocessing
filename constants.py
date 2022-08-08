CRITICAL_RELATIVE_ANGLE = 6.0
CRITICAL_ABSOLUTE_ANGLE = 13.0
ADMISSIBLE_ELEV_DEVIATIONS = {
    "FLATLAND": 3,
    "HILLS": 5,
    "MOUNTAIN": 5
}
NOMINAL_OVERLAPS = {
    "NATURE": {
        "FLATLAND": {
            "LINE": 63,
            "SIDE": 32
        },
        "HILLS": {
            "LINE": 67,
            "SIDE": 35
        },
        "MOUNTAINS": {
            "LINE": 72,
            "SIDE": 40
        }
    },
    "SETTLEMENTS": {
        "0.05": {
            "LINE": 76,
            "SIDE": 60
        },
        "0.10": {
            "LINE": 77,
            "SIDE": 62
        },
        "0.15": {
            "LINE": 79,
            "SIDE": 64
        },
        "0.20": {
            "LINE": 81,
            "SIDE": 67
        },
        "0.25": {
            "LINE": 82,
            "SIDE": 70
        }
    }
}
CRITICAL_OVERLAPS = {
    "FLATLAND": {
        "LINE": {
            "MIN": -7,
            "MAX": 6
        },
        "SIDE": {
            "MIN": -12,
            "MAX": 10
        }
    },
    "HILLS": {
        "LINE": {
            "MIN": -9,
            "MAX": 7
        },
        "SIDE": {
            "MIN": -15,
            "MAX": 12
        }
    },
    "MOUNTAINS": {
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
        'FRAME_SIZE': (7952, 5304),
        'PIXEL_SIZE': 0.0045,
        'SPECTRUM_SIGNATURE': 'RGB',
        'FILE_FORMAT': 'JPEG'
    },
    2: {
        'NAME': 'Sony A6000',
        'SERIAL_NUMBER': 7391829,
        'FOCAL_LENGTH': 20,
        'FRAME_SIZE': (6000, 4000),
        'PIXEL_SIZE': 0.0039,
        'SPECTRUM_SIGNATURE': 'NIR',
        'FILE_FORMAT': 'ARW'
    }
}

AFS_TYPES = {
    1: 'Площадная надирная',
    2: 'Линейная надирная',
    4: 'Площадная перспективная',
    4: 'Линейная перспективная'
}