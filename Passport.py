from os import path as p

class Passport(object):
    """Класс для создания паспорта АФС"""
    def __init__(self, path, objectName, siteName):
        self.path = path
        self.objectName = objectName
        self.siteName = siteName
        self.report = open(p.join(self.path, 'Паспорт АФС_{}_{}.html'.format(objectName, siteName)), 'w')
        self.report.write('<title>Паспорт АФС {} {}</title>\n'.format(objectName, siteName))
        self.report.write(f"""<style>
            h1 {{font-size:16px}}
            table {{border-collapse: collapse;border: 1px solid;}}
            th {{border: 1px solid;}}
            td {{border: 1px solid;}}
        </style>""")
    
    def writeInfo(self, customer, date, startTime, endTime):
        self.date = date
        self.report.write(f"""<h1>ПАСПОРТ АЭРОФОТОСЪЁМКИ</h1>
        <table>
            <tbody>
                <tr>
                    <td>Название или шифр объекта съемки</td>
                    <td>{self.objectName}</td>
                    <td>Съёмочный участок</td>
                    <td>{self.siteName}</td>
                </tr>
                <tr>
                    <td>Исполнитель АФС</td>
                    <td>ГАУ АО "ЦПАПР"</td>
                    <td>Заказчик</td>
                    <td>{customer}</td>
                </tr>
                <tr>
                    <td>Дата и время начала</td>
                    <td>{str(date) + ' ' + str(startTime)}</td>
                    <td>Дата и время окончания</td>
                    <td>{str(date) + ' ' + str(endTime)}</td>
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
        <p>Список номеров концевых маршрутов</p>
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
        

    def closeFile(self):
        self.report.close()

if __name__ == '__main__':
    r = Passport('test', 'Николаевская', '1')
    r.writeInfo('Служба природопользования', '2022-07-21', '10:30:22', '13:45:18')
    r.closeFile()