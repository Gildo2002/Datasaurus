import matplotlib.pyplot as plt
import csv
import numpy as np

ruta = "Datos\DatasaurusDozen.tsv"

with open(ruta, 'r') as File:
    reader = csv.reader(File, dialect=csv.excel_tab)
    headers = next(reader)
    data = list(reader)
    data = np.array(data)
pass

name_graph = ['Dino', 'Away', 'H_lines', 'H_lines', 'X_shape', 'Star',
              'Sigh_lines', 'Dots', 'Circle', 'Bullseye', 'Slant_up',
              'Slant_down', 'Wide_lines']

x0 = np.array(data[0: 142, 1], dtype=float)
y0 = np.array(data[0: 142, 2], dtype=float)

x1 = np.array(data[142: 284, 1], dtype=float)
y1 = np.array(data[142: 284, 2], dtype=float)

x2 = np.array(data[284: 426, 1], dtype=float)
y2 = np.array(data[284: 426, 2], dtype=float)

x3 = np.array(data[426: 568, 1], dtype=float)
y3 = np.array(data[426: 568, 2], dtype=float)

x4 = np.array(data[568: 710, 1], dtype=float)
y4 = np.array(data[568: 710, 2], dtype=float)

x5 = np.array(data[710: 852, 1], dtype=float)
y5 = np.array(data[710: 852, 2], dtype=float)

x6 = np.array(data[852: 994, 1], dtype=float)
y6 = np.array(data[852: 994, 2], dtype=float)

x7 = np.array(data[994: 1136, 1], dtype=float)
y7 = np.array(data[994: 1136, 2], dtype=float)

x8 = np.array(data[1136: 1278, 1], dtype=float)
y8 = np.array(data[1136: 1278, 2], dtype=float)

x9 = np.array(data[1278: 1420, 1], dtype=float)
y9 = np.array(data[1278: 1420, 2], dtype=float)

x10 = np.array(data[1420: 1562, 1], dtype=float)
y10 = np.array(data[1420: 1562, 2], dtype=float)

x11 = np.array(data[1562: 1704, 1], dtype=float)
y11 = np.array(data[1562: 1704, 2], dtype=float)

x12 = np.array(data[1704: 1846, 1], dtype=float)
y12 = np.array(data[1704: 1846, 2], dtype=float)

plt.suptitle(name_graph[0])
plt.scatter(x0, y0)
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.show()


def make_plot(axs):

    ax1 = axs[0, 0]
    ax1.scatter(x1, y1)
    ax1.set_title(name_graph[1])
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)

    ax2 = axs[0, 1]
    ax2.scatter(x2, y2)
    ax2.set_title(name_graph[2])
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)

    ax3 = axs[0, 2]
    ax3.scatter(x3, y3)
    ax3.set_title(name_graph[3])
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.set_xlim(0, 100)
    ax3.set_ylim(0, 100)

    ax4 = axs[0, 3]
    ax4.scatter(x4, y4)
    ax4.set_title(name_graph[4])
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.set_xlim(0, 100)
    ax4.set_ylim(0, 100)

    ax5 = axs[1, 0]
    ax5.scatter(x5, y5)
    ax5.set_title(name_graph[5])
    ax5.set_xlabel('x')
    ax5.set_ylabel('y')
    ax5.set_xlim(0, 100)
    ax5.set_ylim(0, 100)

    ax6 = axs[1, 1]
    ax6.scatter(x6, y6)
    ax6.set_title(name_graph[6])
    ax6.set_xlabel('x')
    ax6.set_ylabel('y')
    ax6.set_xlim(0, 100)
    ax6.set_ylim(0, 100)

    ax7 = axs[1, 2]
    ax7.scatter(x7, y7)
    ax7.set_title(name_graph[7])
    ax7.set_xlabel('x')
    ax7.set_ylabel('y')
    ax7.set_xlim(0, 100)
    ax7.set_ylim(0, 100)

    ax8 = axs[1, 3]
    ax8.scatter(x8, y8)
    ax8.set_title(name_graph[8])
    ax8.set_xlabel('x')
    ax8.set_ylabel('y')
    ax8.set_xlim(0, 100)
    ax8.set_ylim(0, 100)

    ax9 = axs[2, 0]
    ax9.scatter(x9, y9)
    ax9.set_title(name_graph[9])
    ax9.set_xlabel('x')
    ax9.set_ylabel('y')
    ax9.set_xlim(0, 100)
    ax9.set_ylim(0, 100)

    ax10 = axs[2, 1]
    ax10.scatter(x10, y10)
    ax10.set_title(name_graph[10])
    ax10.set_xlabel('x')
    ax10.set_ylabel('y')
    ax10.set_xlim(0, 100)
    ax10.set_ylim(0, 100)

    ax11 = axs[2, 2]
    ax11.scatter(x11, y11)
    ax11.set_title(name_graph[11])
    ax11.set_xlabel('x')
    ax11.set_ylabel('y')
    ax11.set_xlim(0, 100)
    ax11.set_ylim(0, 100)

    ax12 = axs[2, 3]
    ax12.scatter(x12, y12)
    ax12.set_title(name_graph[12])
    ax12.set_xlabel('x')
    ax12.set_ylabel('y')
    ax12.set_xlim(0, 100)
    ax12.set_ylim(0, 100)


# Plot 1:
fig, axs = plt.subplots(3, 4)
fig.subplots_adjust(top=0.9, bottom=0.10, left=0.10, right=0.9, hspace=0.35,
                    wspace=0.35)
make_plot(axs)

# just align the last column of axes:
fig.tight_layout()
plt.show()

print(name_graph[0])
print('Promedio x:', "%.4f" % np.mean(x0),'Promedio y:',"%.4f" % np.mean(y0))
print('Varianza x:', "%.4f" % np.std(x0),'Varianza y:',"%.4f" % np.std(y0))
print('Correlacion x:', "%.4f" % np.corrcoef(x0),'Correlacion y:',"%.4f" % np.corrcoef(y0))

print(name_graph[1])
print('Promedio x:', "%.4f" % np.mean(x1),'Promedio y:',"%.4f" % np.mean(y1))
print('Varianza x:', "%.4f" % np.std(x1),'Varianza y:',"%.4f" % np.std(y1))
print('Correlacion x:', "%.4f" % np.corrcoef(x1),'Correlacion y:',"%.4f" % np.corrcoef(y1))

print(name_graph[2])
print('Promedio x:', "%.4f" % np.mean(x2),'Promedio y:',"%.4f" % np.mean(y2))
print('Varianza x:', "%.4f" % np.std(x2),'Varianza y:',"%.4f" % np.std(y2))
print('Correlacion x:', "%.4f" % np.corrcoef(x2),'Correlacion y:',"%.4f" % np.corrcoef(y2))

print(name_graph[3])
print('Promedio x:', "%.4f" % np.mean(x3),'Promedio y:',"%.4f" % np.mean(y3))
print('Varianza x:', "%.4f" % np.std(x3),'Varianza y:',"%.4f" % np.std(y3))
print('Correlacion x:', "%.4f" % np.corrcoef(x3),'Correlacion y:',"%.4f" % np.corrcoef(y3))

print(name_graph[4])
print('Promedio x:', "%.4f" % np.mean(x4),'Promedio y:',"%.4f" % np.mean(y4))
print('Varianza x:', "%.4f" % np.std(x4),'Varianza y:',"%.4f" % np.std(y4))
print('Correlacion x:', "%.4f" % np.corrcoef(x4),'Correlacion y:',"%.4f" % np.corrcoef(y4))

print(name_graph[5])
print('Promedio x:', "%.4f" % np.mean(x5),'Promedio y:',"%.4f" % np.mean(y5))
print('Varianza x:', "%.4f" % np.std(x5),'Varianza y:',"%.4f" % np.std(y5))
print('Correlacion x:', "%.4f" % np.corrcoef(x5),'Correlacion y:',"%.4f" % np.corrcoef(y5))

print(name_graph[6])
print('Promedio x:', "%.4f" % np.mean(x6),'Promedio y:',"%.4f" % np.mean(y6))
print('Varianza x:', "%.4f" % np.std(x6),'Varianza y:',"%.4f" % np.std(y6))
print('Correlacion x:', "%.4f" % np.corrcoef(x6),'Correlacion y:',"%.4f" % np.corrcoef(y6))

print(name_graph[7])
print('Promedio x:', "%.4f" % np.mean(x7),'Promedio y:',"%.4f" % np.mean(y7))
print('Varianza x:', "%.4f" % np.std(x7),'Varianza y:',"%.4f" % np.std(y7))
print('Correlacion x:', "%.4f" % np.corrcoef(x7),'Correlacion y:',"%.4f" % np.corrcoef(y7))

print(name_graph[8])
print('Promedio x:', "%.4f" % np.mean(x8),'Promedio y:',"%.4f" % np.mean(y8))
print('Varianza x:', "%.4f" % np.std(x8),'Varianza y:',"%.4f" % np.std(y8))
print('Correlacion x:', "%.4f" % np.corrcoef(x8),'Correlacion y:',"%.4f" % np.corrcoef(y8))

print(name_graph[9])
print('Promedio x:', "%.4f" % np.mean(x9),'Promedio y:',"%.4f" % np.mean(y9))
print('Varianza x:', "%.4f" % np.std(x9),'Varianza y:',"%.4f" % np.std(y9))
print('Correlacion x:', "%.4f" % np.corrcoef(x9),'Correlacion y:',"%.4f" % np.corrcoef(y9))

print(name_graph[10])
print('Promedio x:', "%.4f" % np.mean(x10),'Promedio y:',"%.4f" % np.mean(y10))
print('Varianza x:', "%.4f" % np.std(x10),'Varianza y:',"%.4f" % np.std(y10))
print('Correlacion x:', "%.4f" % np.corrcoef(x10),'Correlacion y:',"%.4f" % np.corrcoef(y10))

print(name_graph[11])
print('Promedio x:', "%.4f" % np.mean(x11),'Promedio y:',"%.4f" % np.mean(y11))
print('Varianza x:', "%.4f" % np.std(x11),'Varianza y:',"%.4f" % np.std(y11))
print('Correlacion x:', "%.4f" % np.corrcoef(x11),'Correlacion y:',"%.4f" % np.corrcoef(y11))

print(name_graph[12])
print('Promedio x:', "%.4f" % np.mean(x12),'Promedio y:',"%.4f" % np.mean(y12))
print('Varianza x:', "%.4f" % np.std(x12),'Varianza y:',"%.4f" % np.std(y12))
print('Correlacion x:', "%.4f" % np.corrcoef(x12),'Correlacion y:',"%.4f" % np.corrcoef(y12))