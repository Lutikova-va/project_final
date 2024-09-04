import matplotlib
import matplotlib.pyplot as plt
import sys
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import colors
from matplotlib.colors import LightSource
import numpy as np
from itertools import zip_longest

colors_name = ["salmon", "darkorange", "gold", "springgreen", "cornflowerblue",
               "navy", "darkviolet", "dimgrey", "whitesmoke"]
colors_ru = ["красный", "оранжевый", "желтый", "зеленый", "голубой",
             "синий", "фиолетовый", "черный", "белый"]
current_color_index = 0
shape_index = 0


class RhombicDodPrimaryNormal:
    def __init__(self):
        self.points = [
            [1, 1, 3], [1, 1, 1], [1, -1, 3],
            [1, -1, 1], [-1, 1, 3], [-1, 1, 1],
            [-1, -1, 3], [-1, -1, 1], [0, 0, 4],
            [0, 0, 0], [0, 2, 2], [0, -2, 2],
            [2, 0, 2], [-2, 0, 2]
        ]

        self.surfaces = [
            [self.points[0], self.points[1], self.points[12]],  # front
            [self.points[1], self.points[3], self.points[12]],
            [self.points[3], self.points[2], self.points[12]],
            [self.points[2], self.points[0], self.points[12]],

            [self.points[6], self.points[4], self.points[13]],  # behind
            [self.points[4], self.points[5], self.points[13]],
            [self.points[5], self.points[7], self.points[13]],
            [self.points[7], self.points[6], self.points[13]],

            [self.points[6], self.points[4], self.points[8]],  # top
            [self.points[4], self.points[0], self.points[8]],
            [self.points[0], self.points[2], self.points[8]],
            [self.points[2], self.points[6], self.points[8]],

            [self.points[3], self.points[1], self.points[9]],  # below
            [self.points[1], self.points[5], self.points[9]],
            [self.points[5], self.points[7], self.points[9]],
            [self.points[7], self.points[3], self.points[9]],

            [self.points[0], self.points[4], self.points[10]],  # right
            [self.points[4], self.points[5], self.points[10]],
            [self.points[5], self.points[1], self.points[10]],
            [self.points[1], self.points[0], self.points[10]],

            [self.points[2], self.points[6], self.points[11]],  # left
            [self.points[6], self.points[7], self.points[11]],
            [self.points[7], self.points[3], self.points[11]],
            [self.points[3], self.points[2], self.points[11]]
        ]

    def get_surfaces(self):
        return self.surfaces


class RhombicDodPrimaryConcaveOne:
    def __init__(self):
        self.points = [
            [1, 1, 3], [1, 1, 1], [1, -1, 3],
            [1, -1, 1], [-1, 1, 3], [-1, 1, 1],
            [-1, -1, 3], [-1, -1, 1], [0, 0, 2],
            [0, 0, 0], [0, 2, 2], [0, -2, 2],
            [2, 0, 2], [-2, 0, 2]
        ]

        self.surfaces = [
            [self.points[0], self.points[1], self.points[12]],  # front
            [self.points[1], self.points[3], self.points[12]],
            [self.points[3], self.points[2], self.points[12]],
            [self.points[2], self.points[0], self.points[12]],

            [self.points[6], self.points[4], self.points[13]],  # behind
            [self.points[4], self.points[5], self.points[13]],
            [self.points[5], self.points[7], self.points[13]],
            [self.points[7], self.points[6], self.points[13]],

            [self.points[6], self.points[4], self.points[8]],  # top
            [self.points[4], self.points[0], self.points[8]],
            [self.points[0], self.points[2], self.points[8]],
            [self.points[2], self.points[6], self.points[8]],

            [self.points[3], self.points[1], self.points[9]],  # below
            [self.points[1], self.points[5], self.points[9]],
            [self.points[5], self.points[7], self.points[9]],
            [self.points[7], self.points[3], self.points[9]],

            [self.points[0], self.points[4], self.points[10]],  # right
            [self.points[4], self.points[5], self.points[10]],
            [self.points[5], self.points[1], self.points[10]],
            [self.points[1], self.points[0], self.points[10]],

            [self.points[2], self.points[6], self.points[11]],  # left
            [self.points[6], self.points[7], self.points[11]],
            [self.points[7], self.points[3], self.points[11]],
            [self.points[3], self.points[2], self.points[11]]
        ]

    def get_surfaces(self):
        return self.surfaces


class RhombicDodPrimaryConcaveTwo:
    def __init__(self):
        self.points = [
            [1, 1, 3], [1, 1, 1], [1, -1, 3],
            [1, -1, 1], [-1, 1, 3], [-1, 1, 1],
            [-1, -1, 3], [-1, -1, 1], [0, 0, 2],
            [0, 0, 2], [0, 2, 2], [0, -2, 2],
            [2, 0, 2], [-2, 0, 2]
        ]

        self.surfaces = [
            [self.points[0], self.points[1], self.points[12]],  # front
            [self.points[1], self.points[3], self.points[12]],
            [self.points[3], self.points[2], self.points[12]],
            [self.points[2], self.points[0], self.points[12]],

            [self.points[6], self.points[4], self.points[13]],  # behind
            [self.points[4], self.points[5], self.points[13]],
            [self.points[5], self.points[7], self.points[13]],
            [self.points[7], self.points[6], self.points[13]],

            [self.points[6], self.points[4], self.points[8]],  # top
            [self.points[4], self.points[0], self.points[8]],
            [self.points[0], self.points[2], self.points[8]],
            [self.points[2], self.points[6], self.points[8]],

            [self.points[3], self.points[1], self.points[9]],  # below
            [self.points[1], self.points[5], self.points[9]],
            [self.points[5], self.points[7], self.points[9]],
            [self.points[7], self.points[3], self.points[9]],

            [self.points[0], self.points[4], self.points[10]],  # right
            [self.points[4], self.points[5], self.points[10]],
            [self.points[5], self.points[1], self.points[10]],
            [self.points[1], self.points[0], self.points[10]],

            [self.points[2], self.points[6], self.points[11]],  # left
            [self.points[6], self.points[7], self.points[11]],
            [self.points[7], self.points[3], self.points[11]],
            [self.points[3], self.points[2], self.points[11]]
        ]

    def get_surfaces(self):
        return self.surfaces


class RDChildNormal(RhombicDodPrimaryNormal):
    def __init__(self, x, y, z, current_color_index):
        super().__init__()
        self.x_offset = x
        self.y_offset = y
        self.z_offset = z
        self.color_index = current_color_index

        for i in range(0, 14):
            self.points[i][0] = self.points[i][0] + int(self.x_offset)
            self.points[i][1] = self.points[i][1] + int(self.y_offset)
            self.points[i][2] = self.points[i][2] + int(self.z_offset)

    def color(self):
        return colors_name[self.color_index]

    def get_x_off(self):
        return self.x_offset

    def get_y_off(self):
        return self.y_offset

    def get_z_off(self):
        return self.z_offset

    def get_shape_index(self):
        return 0

    def get_z(self, i):
        return self.points[i][2]


class RDChildConcaveOne(RhombicDodPrimaryConcaveOne):
    def __init__(self, x, y, z, current_color_index):
        super().__init__()
        self.x_offset = x
        self.y_offset = y
        self.z_offset = z
        self.color_index = current_color_index

        for i in range(0, 14):
            self.points[i][0] = self.points[i][0] + int(self.x_offset)
            self.points[i][1] = self.points[i][1] + int(self.y_offset)
            self.points[i][2] = self.points[i][2] + int(self.z_offset)

    def color(self):
        return colors_name[self.color_index]

    def get_x_off(self):
        return self.x_offset

    def get_y_off(self):
        return self.y_offset

    def get_z_off(self):
        return self.z_offset

    def get_shape_index(self):
        return 1

    def get_z(self, i):
        return self.points[i][2]


class RDChildConcaveTwo(RhombicDodPrimaryConcaveTwo):
    def __init__(self, x, y, z, current_color_index):
        super().__init__()
        self.x_offset = x
        self.y_offset = y
        self.z_offset = z
        self.color_index = current_color_index

        for i in range(0, 14):
            self.points[i][0] = self.points[i][0] + int(self.x_offset)
            self.points[i][1] = self.points[i][1] + int(self.y_offset)
            self.points[i][2] = self.points[i][2] + int(self.z_offset)

    def color(self):
        return colors_name[self.color_index]

    def get_x_off(self):
        return self.x_offset

    def get_y_off(self):
        return self.y_offset

    def get_z_off(self):
        return self.z_offset

    def get_z(self, i):
        return self.points[i][2]

    @staticmethod
    def get_shape_index():
        return 2


def choose_color(color_index):
    global current_color_index
    current_color_index = color_index


def update_plot(event=None):
    global rhombic_normal, current_color_index, rhombic_concave_one, rhombic_concave_two
    x_val = x_entry.get()
    y_val = y_entry.get()
    z_val = z_entry.get()

    if x_val.strip() == "" or y_val.strip() == "" or z_val.strip() == "":
        root.after(1000, update_plot)  # Retry after 1 second if any field is empty
        return

    try:
        x_off = int(x_val)
        y_off = int(y_val)
        z_off = int(z_val)
    except ValueError:
        root.after(1000, update_plot)  # Retry after 1 second if invalid input
        return

    if shape_index == 0:
        rhombic_normal.append(RDChildNormal(x_off, y_off, z_off, current_color_index))
    elif shape_index == 1:
        rhombic_concave_one.append(RDChildConcaveOne(x_off, y_off, z_off, current_color_index))
    elif shape_index == 2:
        rhombic_concave_two.append(RDChildConcaveTwo(x_off, y_off, z_off, current_color_index))

    ax.clear()
    max_offset = max(
        max(
            max(abs(child.get_x_off()), abs(child.get_y_off()), abs(child.get_z_off()))
            for child in (child, child_conc_one, child_conc_two) if child is not None
        )
        for child, child_conc_one, child_conc_two in zip_longest(rhombic_normal, rhombic_concave_one,
                                                                 rhombic_concave_two)
    )
    ax.set_xlim3d(-3 - max_offset, 3 + max_offset)
    ax.set_ylim3d(-3 - max_offset, 3 + max_offset)
    ax.set_zlim3d(-3 - max_offset, 3 + max_offset)

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    for normal in rhombic_normal:
        ax.add_collection3d(Poly3DCollection(normal.get_surfaces(), facecolors=normal.color(), edgecolors='plum'))
    for concave_one in rhombic_concave_one:
        ax.add_collection3d(Poly3DCollection(concave_one.get_surfaces(), facecolors=concave_one.color(), edgecolors='plum'))
    for concave_two in rhombic_concave_two:
        ax.add_collection3d(Poly3DCollection(concave_two.get_surfaces(), facecolors=concave_two.color(), edgecolors='plum'))

    canvas.draw()

    x_entry.bind("<Return>", update_plot)
    y_entry.bind("<Return>", update_plot)
    z_entry.bind("<Return>", update_plot)


def leave():
    sys.exit()


def choose_shape(current_shape):
    global shape_index
    shape_index = current_shape


rhombic_normal = []
rhombic_concave_one = []
rhombic_concave_two = []
rhombic1 = RhombicDodPrimaryNormal()
LARGEFONT = ("Verdana", 25)

root = tk.Tk()
root.title("конструктор")

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=0)

x_label = tk.Label(root, text="вершина по х:")
x_entry = tk.Entry(root)
x_label.grid(row=1, column=1, pady=2)
x_entry.grid(row=1, column=2, pady=2)

y_label = tk.Label(root, text="вершина по у:")
y_entry = tk.Entry(root)
y_label.grid(row=2, column=1, pady=2)
y_entry.grid(row=2, column=2, pady=2)

z_label = tk.Label(root, text="вершина по z:")
z_entry = tk.Entry(root)
z_label.grid(row=3, column=1, pady=2)
z_entry.grid(row=3, column=2, pady=2)

qbut = tk.Button(root, text="выйти", command=leave)
qbut.grid(row=5, column=0, pady=2)

for i, color in enumerate(colors_name):
    button = tk.Button(root, text=colors_ru[i], command=lambda
        i=i: choose_color(i))
    button.grid(row=1 + i // 3, column=3 + i % 3, pady=2)

switch_normal = tk.Button(root, text="нормальный", command=lambda: choose_shape(0))
switch_concave = tk.Button(root, text="вогнутый с одной стороны", command=lambda: choose_shape(1))
switch_concave_two = tk.Button(root, text="вогнутый с двух сторон", command=lambda: choose_shape(2))
switch_normal.grid(row=5, column=1, pady=2)
switch_concave.grid(row=5, column=2, pady=2)
switch_concave_two.grid(row=5, column=3, pady=2)
update_plot()
root.mainloop()