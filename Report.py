from os import path as p

class Report(object):
    """
    Класс для создания отчётов
    """
    def __init__(self, path, fileName):
        self.path = path
        self.fileName = fileName
        self.report = open(p.join(self.path, self.fileName), 'w')
        self.report.write('\t\tОТЧЕТ\n\t\tКОНТРОЛЬ КАЧЕСТВА АЭРОФОТОСЪЁМКИ\n\n')
    
    def writeInfo(self, objectName, siteName, date, startTime, endTime):
        self.report.write('\tОбъект:\t\t\t{}\n'.format(objectName))
        self.report.write('\tСъёмочный участок:\t{}\n'.format(siteName))
        self.report.write('\tДата:\t\t\t{}\n'.format(date))
        self.report.write('\tВремя начала:\t\t{}\n'.format(startTime))
        self.report.write('\tВремя окончания:\t{}\n'.format(endTime))

    def closeFile(self):
        self.report.close()

if __name__ == '__main__':
    r = Report('/home/owgrant/Документы/Работа/Данные_для_тестирования_плагинов_QGIS/', 'report.txt')
    r.writeInfo('Протока Николаевская', '1', '2022-07-21', '10:30:22', '13:45:18')
    r.closeFile()