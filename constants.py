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