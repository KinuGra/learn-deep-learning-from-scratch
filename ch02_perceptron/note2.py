import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # 重みとバイアスだけがANDと違う
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  # 重みとバイアスだけが AND と違う
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


if __name__ == "__main__":
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

    print("AND")
    for x1, x2 in inputs:
        print(f"  ({x1}, {x2}) -> {AND(x1, x2)}")

    print("NAND")
    for x1, x2 in inputs:
        print(f"  ({x1}, {x2}) -> {NAND(x1, x2)}")

    print("OR")
    for x1, x2 in inputs:
        print(f"  ({x1}, {x2}) -> {OR(x1, x2)}")
