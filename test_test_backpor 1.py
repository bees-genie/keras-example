import sys

EPOCH = 3000
LR = 0.005

x1, x2 = 0.05, 0.10
w1, w2, w3, w4, w5, w6 = 0.15, 0.20, 0.35, 0.30, 0.45, 0.55  # 수정: 6개의 가중치 추가
b, b1, b2 = 0.35, 0.3, 0.6
yt1, yt2, yt3 = 0.1, 0.99, 0.5
lr = LR

for epoch in range(EPOCH):
    # Forward Pass
    y1 = x1 * w1 + x2 * w2 + b
    y2 = x1 * w3 + x2 * w4 + b1 
    y3 = y1 * w5 + y2 * w6 + b2   # Loss 계산
    e1 = (y1 - yt1) ** 2 / 2
    e2 = (y2 - yt2) ** 2 / 2
    e3 = (y3 - yt3) ** 2 / 2

    # Error 계산
    yE1 = y1 - yt1
    yE2 = y2 - yt2
    yE3 = y3 - yt3

    # Backpropagation
    w1 -= lr * yE1 * x1
    w2 -= lr * yE1 * x2
    b1 -= lr * yE1
    w3 -= lr * yE2 * x1
    w4 -= lr * yE2 * x2
    b2 -= lr * yE2
    w5 -= lr * yE3 * y1
    w6 -= lr * yE3 * y2
    b -= lr * yE3

    if e1 < 0.000000000001 and e2 < 0.000000000001 and e3 < 0.000000000001:
        break

print(f"epoch = {epoch}")
print(f"y1: {y1:.3f}")
print(f"y2: {y2:.3f}")
print(f"y3: {y3:.3f}")
print(f"w1: {w1:.3f}")
print(f"w2: {w2:.3f}")
print(f"w3: {w3:.3f}")
print(f"w4: {w4:.3f}")
print(f"w5: {w5:.3f}")
print(f"w6: {w6:.3f}")
print(f"b: {b:.3f}")
print(f"b1: {b1:.3f}")
print(f"b2: {b2:.3f}")