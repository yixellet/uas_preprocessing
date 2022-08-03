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
        with open(rinex, 'r') as rnx, \
             open(marksRGB, 'r') as mrxRGB, \
             open(marksNIR, 'r') as mrxNIR, \
             open(rinex[:-8] + 'RX1RM2.22o.obs', 'w') as rnxRGB, \
             open(rinex[:-8] + 'A6000.22o.obs', 'w') as rnxNIR:
            marksRGBArray = marksToArray(mrxRGB)
            marksNIRArray = marksToArray(mrxNIR)
            for line in rnx:
                if line[2:] not in marksRGBArray:
                    rnxNIR.write(line)
                if line[2:] not in marksNIRArray:
                    rnxRGB.write(line)

if __name__ == "__main__":
    sr = SplitRinex()
    sr.splitRinex('test/rinex/2022_07_26_g201b20445_f003_.22o copy.obs',
    'test/rinex/2022_07_26_SonyRX1RM2_g201b20445_f003.marks',
    'test/rinex/2022_07_26_SonyA6000_g201b20445_f003.marks')