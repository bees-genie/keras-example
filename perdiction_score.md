# Prediction , Recall Accuracy

 * perdiction, recall, accuracy 는 model을 평가 하기위한 요소, 수치화한 지표이다.

 # Model 분류와 정답
  
모델을 평가하는 요소는 결국, 모델이 내놓은 답과 실제 정답의 관계로써 정의를 내릴 수 있습니다.

![Model 분류와 정답 cofusion matrix](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99DC064C5BE056CE10 "Model 분류와 정답 cofusion matrix")

- True Positive(TP) : 실제 True인 정답을 True라고 예측 (정답)

- False Positive(FP) : 실제 False인 정답을 True라고 예측 (오답)

- False Negative(FN) : 실제 True인 정답을 False라고 예측 (오답)


- True Negative(TN) : 실제 False인 정답을 False라고 예측 (정답)

# perdiction (Positive Predictive Value)
- 정밀도란 모델이 True라고 분류한 것 중에서 실제 True인 것의 비율

![Precision 식](https://t1.daumcdn.net/cfile/tistory/99F66B345BE0596109 "Precision")

# Recall 

- 재현율이란 실제 True인 것 중에서 모델이 True라고 예측한 것의 비율

![Recall 식](https://t1.daumcdn.net/cfile/tistory/997188435BE05B0628 "Recall eq")    

Precision은 모델의 입장에서, 그리고 Recall은 실제 정답(data)의 입장에서 정답을 정답이라고 맞춘 경우를 바라보고 있습니다.

# Precision-Recall Trade-off
![Recall 식](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FvRV1U%2Fbtq8IEu6j1f%2FNEVedeLCa5uzDZMMrIsWG0%2Fimg.png "Recall eq")

- Type 1, 2 error에 해당하는 FN, FP를 더하여 계산합니다. 이때, FN, FP는 각각 Type 1, 2 error에 있으므로 Precision과 Recall 또한 trade-off 관계에 있다고 할 수 있습니다.

#  Accuracy(정확도)

- 모두 True를 True라고 옳게 예측한 경우에 대해서만 다루었습니다. 하지만, False를 False라고 예측한 경우도 옳은 경우입니다. 이때, 해당 경우를 고려하는 지표가 바로 정확도(Accuracy)
![alt text](image.png)

#  F1 score

- F1 score는 Precision과 Recall의 조화평균

![alt text](image-1.png)

# Fall-out

- Fall-out은 FPR(False Positive Rate)으로도 불리며, 실제 False인 data 중에서 모델이 True라고 예측한 비율

![ ](image-2.png)

# ROC(Receiver Operating Characteristic) curve
- 임계값들을 기준으로 Recall-Fallout의 변화를 시각화한 것입니다. Fallout은 실제 False인 data 중에서 모델이 True로 분류한, 그리고 Recall은 실제 True인 data 중에서 모델이 True로 분류한 비율을 나타낸 지표로써, 이 두 지표를 각각 x, y의 축으로 놓고 그려지는 그래프
![alt text](image-3.png)

# AUC(Area Under Curve)

- ROC curve는 그래프이기 때문에 명확한 수치로써 비교하기가 어렵습니다. 따라서 그래프 아래의 면적값을 이용합니다. 이것이 바로 AUC(Area Under Curve)입니다. 최대값은 1이며 좋은 모델(즉, Fall-out에 비해 Recall 값이 클수록) 1에 가까운 값이 나옵