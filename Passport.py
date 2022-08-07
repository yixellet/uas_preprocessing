from os import path as p

from constants import AFS_TYPES
from styles import passport_style

class Passport(object):
    """Класс для создания паспорта АФС"""
    def __init__(self, path, objectName, siteName):
        self.path = path
        self.objectName = objectName
        self.siteName = siteName
        self.report = open(p.join(p.split(self.path)[0], 'Паспорт АФС_{}_{}.html'.format(objectName, siteName)), 'w')
        self.report.write('<title>Паспорт АФС {} {}</title>\n'.format(objectName, siteName))
        self.report.write(passport_style)
    
    def writeInfo(self, customer, date, startTime, endTime, relief_type, 
                  afs_type, size, routes_orientation, line_overlap, side_overlap,
                  altitude, ground_pixel_size, camera, receiver, uav):
        self.date = date
        afs_type_property = 'Площадь АФС, кв.км.' if afs_type == 1 or afs_type == 3 else 'Протяженность АФС, км'
        self.report.write(f"""<h1>ПАСПОРТ АЭРОФОТОСЪЁМКИ</h1>
        <table>
            <tbody>
                <tr>
                    <th>Название или шифр объекта съемки</th>
                    <td>{self.objectName}</td>
                    <th>Съёмочный участок</th>
                    <td>{self.siteName}</td>
                </tr>
                <tr>
                    <th>Исполнитель АФС</th>
                    <td>ГАУ АО "ЦПАПР"</td>
                    <th>Заказчик</th>
                    <td>{customer}</td>
                </tr>
                <tr>
                    <th>Дата и время начала</th>
                    <td>{str(date) + ' ' + str(startTime)}</td>
                    <th>Дата и время окончания</th>
                    <td>{str(date) + ' ' + str(endTime)}</td>
                </tr>
                <tr>
                    <th>Характер местности</th>
                    <td>{relief_type}</td>
                    <th>Вид аэрофотосъёмки</th>
                    <td>{AFS_TYPES[afs_type]}</td>
                </tr>
                <tr>
                    <th colspan="3">{afs_type_property}</th>
                    <td>{size}</td>
                </tr>
                <tr>
                    <th colspan="3">Ориентация маршрутов</th>
                    <td>{routes_orientation}</td>
                </tr>
                <tr>
                    <th>Продольное перекрытие, %</th>
                    <td>{line_overlap}</td>
                    <th>Поперечное перекрытие, %</th>
                    <td>{side_overlap}</td>
                </tr>
                <tr>
                    <th>Высота фотографирования, м</th>
                    <td>{altitude}</td>
                    <th>Номинальное пространственное разрешение, м</th>
                    <td>{ground_pixel_size}</td>
                </tr>
                <tr>
                    <th>Модель аэрофотокамеры</th>
                    <td>{camera['NAME']}</td>
                    <th>Серийный номер аэрофотокамеры</th>
                    <td>{camera['SERIAL_NUMBER']}</td>
                </tr>
                <tr>
                    <th colspan="3">Наличие и тип компенсации продольного сдвига изображения</th>
                    <td>-</td>
                </tr>
                <tr>
                    <th>Фокусное расстояние объектива, мм</th>
                    <td>{camera['FOCAL_LENGTH']}</td>
                    <th>Тип и серийный номер объектива (если он заменяемый)</th>
                    <td>-</td>
                </tr>
                <tr>
                    <th>Размер кадра Nx, пикс</th>
                    <td>{camera['FRAME_SIZE'][0]}</td>
                    <th>Размер кадра Ny, пикс</th>
                    <td>{camera['FRAME_SIZE'][1]}</td>
                </tr>
                <tr>
                    <th>Физический размер пикселя, мм</th>
                    <td>{camera['PIXEL_SIZE']}</td>
                    <th>Ориентация системы координат снимка</th>
                    <td>{camera['COORD_SYS']}</td>
                </tr>
                <tr>
                    <th>Тип аэрофотоустановки (гироплатформы)</th>
                    <td>-</td>
                    <th>Серийный номер аэрофотоустановки (гироплатформы)</th>
                    <td>-</td>
                </tr>
                <tr>
                    <th colspan="3">Спектральная характеристика аэрофотоснимков</th>
                    <td>{camera['SPECTRUM_SIGNATURE']}</td>
                </tr>
                <tr>
                    <th colspan="3">Формат представления цифрового изображения</th>
                    <td>{camera['FILE_FORMAT']}</td>
                </tr>
                <tr>
                    <th>Лидар (тип)</th>
                    <td>-</td>
                    <th>Лидар (серийный номер)</th>
                    <td>-</td>
                </tr>
                <tr>
                    <th colspan="3">Блок определения положения и ориентации (тип, модель, состав)</th>
                    <td>ИИУ</td>
                </tr>
                <tr>
                    <th colspan="3">ГНСС-приёмник (тип, модель)</th>
                    <td>{receiver}</td>
                </tr>
                <tr>
                    <th colspan="3">Воздушное судно</th>
                    <td>{uav}</td>
                </tr>
                <tr>
                    <th colspan="3">Дополнительные сведения по требованию ТЗ</th>
                    <td>-</td>
                </tr>
            </tbody>
        </table>""")
    
    def writeRoutes(self, routes):
        t = ''
        for i in range(len(routes)-1):
            t += f"""
                <tr>
                    <td>{self.date}</td>
                    <td>{i+1}</td>
                    <td>{routes[i]['azimuth'][1]}</td>
                    <td>{routes[i]['photos'][0].name + ' ' + routes[i]['photos'][-1].name}</td>
                    <td></td>
                    <td></td>
                </tr>
            """
        self.report.write(f"""
        <h2 class="routes_list">Список номеров концевых маршрутов</h2>
        <table>
            <tr>
                <th>Дата аэрофотосъемки</th>
                <th>Номер маршрута</th>
                <th>Курс</th>
                <th>Номера концевых снимков</th>
                <th>Номера концевых снимков повторной АФС</th>
                <th>Замечания</th>
            </tr>
            {t}
        </table>
        """)
        
    def closeFile(self, realizer, controller):
        self.report.write('<p>Качество материало аэрофотосъёмочной продукции соответствует ТЗ и требованиям к АФС</p>')
        self.report.write("""<div class="signature">
            <div>Исполнитель АФС</div>
            <div>
                <p>{}</p>
                <p>{}</p>
            </div>
        </div>
        <div class="signature">
            <div>Технический контроль выполнил</div>
            <div>
                <p>{}</p>
                <p>{}</p>
            </div>
        </div>""".format(realizer[0], realizer[1], controller[0], controller[1]))
        self.report.close()

if __name__ == '__main__':
    r = Passport('test', 'Николаевская', '1')
    r.writeInfo('Служба природопользования', '2022-07-21', '10:30:22', '13:45:18')
    r.closeFile()