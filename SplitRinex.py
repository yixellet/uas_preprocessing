def marksToArray(marksFile):
    marksArray = []
    for line in marksFile:
        temp = line.strip().split(' ')
        temp[0] = "2022"
        for i in range(1, 6):
            if temp[i][0] == '0':
                var = ' '+ temp[i][1:]
                temp[i] = var
        marksArray.append(' '.join(temp) + '\n')
    return marksArray

class SplitRinex(object):
    def splitRinex(self, rinex, marksRGB, marksNIR):
        with open(rinex, 'r', encoding='latin-1') as rnx, \
             open(marksRGB, 'r') as mrxRGB, \
             open(marksNIR, 'r') as mrxNIR, \
             open(rinex[:-8] + 'RX1RM2.22o.obs', 'w', encoding='utf-8') as rnxRGB, \
             open(rinex[:-8] + 'A6000.22o.obs', 'w', encoding='utf-8') as rnxNIR:
            marksRGBArray = marksToArray(mrxRGB)
            marksNIRArray = marksToArray(mrxNIR)
            for line in rnx:
                if line[2:] not in marksRGBArray:
                    rnxNIR.write(line)
                if line[2:] not in marksNIRArray:
                    rnxRGB.write(line)

if __name__ == "__main__":
    sr = SplitRinex()
    sr.splitRinex('E:\\ГЕОДЕЗИЯ\\АЭРОФОТОСЪЕМКА\\Водоохранные зоны\\Табола\\2\\2022_08_10_g201b20445_f002_.22o.obs',
    'E:\\ГЕОДЕЗИЯ\\АЭРОФОТОСЪЕМКА\\Водоохранные зоны\\Табола\\2\\2022_08_10_SonyRX1RM2_g201b20445_f002.marks',
    'E:\\ГЕОДЕЗИЯ\\АЭРОФОТОСЪЕМКА\\Водоохранные зоны\\Табола\\2\\2022_08_10_SonyA6000_g201b20445_f002.marks')