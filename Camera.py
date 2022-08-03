class Camera(object):
    """Параметры фотокамеры"""
    def __init__(self, f: int, 
                pixelSize: float, 
                frameWidth: int, 
                frameHeight: int, 
                angleOfView: float,
                spectralChar: str) -> None:
        self.f = f
        self.pixelSize = pixelSize
        self.frameWidth = frameWidth
        self.frameHeight = frameHeight
        self.angleOfView = angleOfView
        self.spectralChar = spectralChar