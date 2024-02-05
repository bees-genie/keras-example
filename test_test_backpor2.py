import sys

EPOCH = 3000
LR = 0.005

x1,x2,x3 = 0.02,0.05,0.12
w1,w2,w3,w4,w5,w6 = 0.15,0.2,0.02,0.27,0.37,0.52
b1,b2 = 0.12,0.39

y1T, y2T = 0.02, 0.98
lr = LR

for epoch in range(EPOCH):
    # Forward Pass
    y1 = x1 * w1 + x2 * w2 + w3*x3 +b1
    y2 = x1 * w4 + x2 *w5 + w6*x3 +b2  
  
    e1 = (y1 - y1T) ** 2 / 2
    e2 = (y2 - y2T) ** 2 / 2
    

    # Error 계산
    yE1 = y1 - y1T
    yE2 = y2 - y2T
    

    # Backpropagation
    w1 -= lr * yE1 * x1
    w2 -= lr * yE1 * x2
    w3 -= lr * yE1 * x3
    b1 -= lr * yE1
    w4 -= lr * yE2 * x1
    w5 -= lr * yE2 * x2
    w6 -= lr * yE2 * x3
    b2 -= lr * yE2
  

    if e1 < 0.000000000001 and e2 < 0.000000000001 :
        break

print(f"epoch = {epoch}")
print(f"y1: {y1:.3f}")
print(f"y2: {y2:.3f}")
print(f"w1: {w1:.3f}")
print(f"w2: {w2:.3f}")
print(f"w3: {w3:.3f}")
print(f"w4: {w4:.3f}")
print(f"w5: {w5:.3f}")
print(f"w6: {w6:.3f}")
print(f"b1: {b1:.3f}")
print(f"b2: {b2:.3f}")