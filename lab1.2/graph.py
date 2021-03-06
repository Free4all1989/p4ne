from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

shA = sheet['A'][1:]
shC = sheet['C'][1:]
shD = sheet['D'][1:]


def getvalue(x):
    return x.value


list_y = list(map(getvalue, shA))
list_x1 = list(map(getvalue, shC))
list_x2 = list(map(getvalue, shD))
pyplot.plot(list_y, list_x1, label="Temp")
pyplot.plot(list_y, list_x2, label="Active")
pyplot.show()
