# 단일 신경망
import sys

EPOCH = 3000#int(sys.argv[1])
LR = 0.005#float(sys.argv[2])

x = 2
w =3
b =1
yt =1
lr =LR

for epoch in range(EPOCH):
    y = x*w + b
    e= (y-yt)**2/2
    yE = y-yt
    wE= yE*x
    bE= yE
    w = w - lr*wE
    w-= lr*wE
    b-=lr *bE

    if e<0.000000000001:
        break

print(f"epoch = {epoch}")
print(f"y: {y:3f}")
print(f"w: {w:3f}")
print(f"b:{b:3f}")