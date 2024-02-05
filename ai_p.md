# 2024.02.05 
## tensorflow 
* 구글이 개발한 머신러닝 프레임워크
* keras 와 함께 사용 가능.

## troch 
* 페이스북이 개발한 머신러닝 프레임워크
* 최근 엔비디아와 협력 중.

# 이미지 분류
* cifar-10, mnist , imagenet, coco data 등.


# Loss fuction

* 알고리즘이 예측한 값과 실제 정답의 차이를 비교하기 위한 함수

loss 함수의 종료.

* MSE(Mean Squared Error)
![MSE 수식](https://velog.velcdn.com/images%2Frcchun%2Fpost%2Fac220735-2d93-46e0-8812-d9772b191c85%2Fimage.png "MSE 수식")

예측한 값과 실제 값 사이의 평균 제곱 오차를 정의한다. 공식이 매우 간단하며, 차가 커질수록 제곱 연산으로 인해서 값이 더욱 뚜렷해진다. 그리고 제곱으로 인해서 오차가 양수이든 음수이든 누적 값을 증가

* RMSE(Root Mean Squared Error)

![MSE 수식](https://velog.velcdn.com/images%2Frcchun%2Fpost%2F1b023dc8-c9ef-4be8-bab1-de4a49ff039c%2Fimage.png "MSE 수식")

MSE에 루트(√)를 씌운 것으로 MSE와 기본적으로 동일하다
MSE에 루트를 씌운 RMSE 은 값의 왜곡을 줄여준다.


* Binary Crossentropy

2개의 레이블 클래스(0, 1로 가정)가 있을 때 Binary Crossentropy를 사용하면 좋다.

![Binary Crossentropy 수식](https://velog.velcdn.com/images%2Frcchun%2Fpost%2F38421275-c6af-41f5-8514-f4bbc815f6aa%2Fimage.png "Binary Crossentropy 수식")

아래 함수에 예측값(Yi) 과 실제값(ti) 에 1을 대입하면, 수식은 0에 수렴하게 됨
아래 함수에 예측값(Yi =0)과 실제값(ti = 1)을 대입한다면, 수식은 양의 무한대가 됨
* keras version
~~~  
tf.keras.losses.BinaryCrossentropy(from_logits=False, label_smoothing=0, reduction="auto", name="binary_crossentropy")
~~~
* torch version
~~~
import torch
import torch.nn as nn

ce_loss = nn.CrossEntropyLoss()
outputs = torch.randn(3, 5, requires_grad = True)
targets = torch.tensor([1, 0, 3], dtype = torch.int64)
loss = ce_loss(outputs, targets)
print(loss)
~~~

* Sparse categorical crossentropy

멀티 클래스 분류에 사용 one-hot encoding 된 상태일 필요 없이 정수 인코딩 된 상태에서 수행 가능.

![categorical crossentropy 수식](https://velog.velcdn.com/images%2Frcchun%2Fpost%2Fbc1b41b8-ffb4-443a-b54e-e04e7fd236ce%2Fimage.png "categorical crossentropy수식")
![categorical crossentropy 수식](https://velog.velcdn.com/images%2Frcchun%2Fpost%2F87602861-f0dc-4175-82cc-020111d32f58%2Fimage.png "categorical crossentropy 수식")

