import sys

EPOCH = 3000
LR = 0.005

x, x1 = 2, 3
w, w1, w2, w3,w4,w5,w6 = 3, 4
b = 1
yt = 27
lr = LR

for epoch in range(EPOCH):
    y = x * w + x1 * w1 + b
    e = (y - yt) ** 2 / 2
    yE = y - yt
    wE = yE * x
    wE1 = yE * x1
    bE = lr * yE
    w -= lr * wE
    w1 -= lr * wE1
    b -= bE

    if e < 0.000000000001:
        break

print(f"epoch = {epoch}")
print(f"y: {y:.3f}")
print(f"w: {w:.3f}")
print(f"w1: {w1:.3f}")
print(f"b:{b:.3f}")