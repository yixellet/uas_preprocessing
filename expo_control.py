from PIL import Image

def expo_control(image):
    res = []
    with Image.open(image) as im:
        if (((im.getextrema()[0][1] - im.getextrema()[0][0]) / 256 < 0.75 and (im.getextrema()[0][1] - im.getextrema()[0][0]) / 256 > 0.99) or 
            ((im.getextrema()[1][1] - im.getextrema()[1][0]) / 256 < 0.75 and (im.getextrema()[1][1] - im.getextrema()[1][0]) / 256 > 0.99) or
            ((im.getextrema()[2][1] - im.getextrema()[2][0]) / 256 < 0.75 and (im.getextrema()[2][1] - im.getextrema()[2][0]) / 256 > 0.99)): 
            res.append([image, round((im.getextrema()[0][1] - im.getextrema()[0][0]) / 256, 2), round((im.getextrema()[1][1] - im.getextrema()[1][0]) / 256, 2), round((im.getextrema()[2][1] - im.getextrema()[2][0]) / 256, 2)])
        else:
            res = 'OK'
    return res