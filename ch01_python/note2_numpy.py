import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))
y = np.array([4.0, 5.0, 6.0])
print(x + y, x / y, x * y)

A = np.array([[1, 2], [3, 4]])
print(A, A.shape, A.dtype, "\n")
B = np.array([[3, 0], [0, 6]])
print(A + B, "\n", A * B)

# ブロードキャストが行われ、形状の異なる配列同士でも演算できる
print(A * 10)
print(x * 2)

C = np.array([[1, 2], [3, 4]])
D = np.array([10, 20])
print(C * D, "\n")

Z = np.array([[51, 52], [14, 19], [0, 4]])
print(Z)
print(Z[0], Z[0][1], "\n")

for row in Z:
    print(row)

Z = Z.flatten()  # 1次元配列に変換
print(Z)
print(Z[np.array([0, 2, 4])])

print(Z > 10)
print(Z[Z > 10])
