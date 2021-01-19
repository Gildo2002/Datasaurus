import numpy as np
import csv
import matplotlib.pyplot as plt
from tabulate import tabulate

ruta = "Datos/DatasaurusDozen.tsv"

# method used to adjustment the windows on diferent monitors y resolutions
# x and y parameters adjust the values between 0 and 2. Default = 1
# info = True, print display resolutions to terminal


def readjustment(x=1, y=1, info=False):
    F = plt.gcf()
    Size = F.get_size_inches()
    if info:
        print("default resolution:      ", "%.2f" %
              Size[0], "x", "%.2f" % Size[1])
        print("readjustment resolution: ", "%.2f" %
              (Size[0] * x), "x", "%.2f" % (Size[1] * y))
    # Set forward to True to resize window along with plot in figure.
    F.set_size_inches(Size[0] * x, Size[1] * y, forward=True)


# Reads the file and assign the values to a list
with open(ruta, 'r') as File:
    reader = csv.reader(File, dialect=csv.excel_tab)
    headers = next(reader)
    data = list(reader)
pass

# Names of the different graphics
name_graph = ['Dino', 'Away', 'H_lines', 'V_lines', 'X_shape', 'Star',
              'High_lines', 'Dots', 'Circle', 'Bullseye', 'Slant_up',
              'Slant_down', 'Wide_lines']

# Colors palette
colors = np.array(["red", "green", "blue", "pink", "black",
                   "orange", "purple", "coral", "indigo", "brown", "gray", "cyan", "magenta"])

name_headers = ['Name', 'X promedio', 'Y promedio', 'X estandar', 'Y estandar', 'Correlacion']

size_x = int(len(data) / len(name_graph))
size_y = len(name_graph)

# Variables vectors will store the value of the coordinates x and y
vectorX = np.empty(shape=(size_x, size_y), dtype=float)
vectorY = np.empty(shape=(size_x, size_y), dtype=float)

i = 0  # counter of the For loop
valuesX = []
valuesY = []

# Passing the values from the list to vectorX and vectorY
for name in name_graph:

    valuesX.clear()
    valuesY.clear()

    for datos in data:
        if name.lower() == datos[0]:
            valuesX.append(datos[1])
            valuesY.append(datos[2])

    vectorX[:, i] = valuesX
    vectorY[:, i] = valuesY

    i = i + 1

# Plot 1: Dino
readjustment(1.5, 1.5)
plt.suptitle(name_graph[0])
plt.scatter(vectorX[:, 0], vectorY[:, 0], c=colors[0])
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.show()

# Plot 2: Other plots
fig, axs = plt.subplots(3, 4)

i = 1
for ax, name in zip(axs.flat, name_graph[1:]):
    ax.scatter(vectorX[:, i], vectorY[:, i], c=colors[i])
    ax.set_title(name)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    i += 1
    pass

# just align the last column of axes:
readjustment(1.5, 1.5)
fig.tight_layout()
plt.show()
plt.close('all')

table_values = []

for i in range(0,len(name_graph)):
    lista = []
    a = [vectorX[:,i]]
    b = [vectorY[:,i]]
    lista.append(name_graph[i])
    lista.append("%.6f" % np.mean(a))
    lista.append("%.6f" % np.mean(b))
    lista.append("%.6f" % np.std(a,ddof=1))
    lista.append("%.6f" % np.std(b,ddof=1))
    lista.append("%.6f" % np.corrcoef(a,b)[0,1])
    table_values.append(lista)


print(tabulate(table_values, headers=name_headers))