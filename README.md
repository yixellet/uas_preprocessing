# Предобработка беспилотной АФС
### Первичная обработка материалов беспилотной аэрофотосъёмки

Скрипт предназначен для полевого послеполётного контроля результатов съёмки, выполненной БВС Геоскан 201 Аэрогеодезия.

## Входные данные:
1. файл телеметрии,
2. файл бортовых ГНСС-наблюдений в формате RINEX,
3. файл меток внешних событий для левой камеры,
4. файл меток внешних событий для правой камеры.

## Скрипт выполняет следующие функции:

1. Выполняет контроль фотограмметрического качества АФС по данным файла телеметрии в соответствии с ГОСТ Р 59328-2021, п.9.
2. Составляет подробный отчёт по результатам контроля.
3. Составляет паспорт АФС в соответствии с ГОСТ Р 59328-2021, приложение Е.
4. Делит бортовой RINEX-файл на два - отдельно для левой и правой камеры.

## Контроль фотограмметрического качества АФС

В алгоритме контроля качества допущены некоторые отклонения от предписаний ГОСТа.

Так, в связи с невозможностью обработки в поле бортовых спутниковых наблюдений невозможно и получение точной фактической высоты фотографирования. По этой причине отклонения высоты расчитываются от среднего значения, полученного из файла телеметрии. При этом предполагается, что полет был выполнен на одной высоте.

Отклонения продольного и поперечного перекрытий следует считать условными по двум причинам:
1. необходимый для расчёта размер снимка на земле получен экспериментально, действительный размер можно получить только после фотограмметрической обработки;
2. углы поворота снимков делают смежные снимки очень далёкими от параллельности;
3. углы крена, тангажа и рысканья имеют достаточно неточные значения.