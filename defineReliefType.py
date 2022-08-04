def defineReliefType(territory_type: int, flight_alt: int, delta_elev: int):
    """Определяет тип рельефа.
    
    Вычисляет отношение перепада высот на объекте к высоте фотографирования
    и определяет тип рельефа
    """
    ratio = delta_elev / flight_alt
    return_value = 0
    if territory_type == 1:
        if ratio <= 0.07:
            return_value = 1
        elif ratio > 0.07 and ratio <= 0.15:
            return_value = 2
        else:
            return_value = 3
    elif territory_type == 2:
        if ratio <= 0.05:
            return_value = 4
        elif ratio > 0.05 and ratio <= 0.1:
            return_value = 5
        elif ratio > 0.1 and ratio <= 0.15:
            return_value = 6
        elif ratio > 0.15 and ratio <= 0.2:
            return_value = 7
        elif ratio > 0.2 and ratio <= 0.25:
            return_value = 8
    return return_value