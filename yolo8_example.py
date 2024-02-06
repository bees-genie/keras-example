# import ultralytics
# ultralytics.checks()
# from PIL import Image

# with Image.open('C:/Users/user/Desktop/test1.jpg') as test_image:
#     test_image.show()
# with Image.open('C:/Users/user/Desktop/test2.jpg') as test_image:
#     test_image.show()
# with Image.open('C:/Users/user/Desktop/test3.jpg') as test_image:
#     test_image.show()
# with Image.open('C:/Users/user/Desktop/test4.jpg') as test_image:
#     test_image.show()

from ultralytics import YOLO
from PIL import Image
from IPython.display import display


model = YOLO('yolov8n.pt')        
print(type(model.names), len(model.names))

print(model.names)

results = model.predict(source='C:/Users/user/Desktop/test/*.jpg', save=True)

with Image.open('C:/Users/user/Desktop/test/test1.jpg') as pred_image:
    display(pred_image)

import numpy as np

for result in results:
        
    uniq, cnt = np.unique(result.boxes.cls.cpu().numpy(), return_counts=True)  # Torch.Tensor -> numpy
    uniq_cnt_dict = dict(zip(uniq, cnt))

    print('\n{class num:counts} =', uniq_cnt_dict,'\n')

    for c in result.boxes.cls:
        print('class num =', int(c), ', class_name =', model.names[int(c)])


import glob

detetced_image_list = glob.glob(('C:/Users/user/Desktop/test/*.jpg'))

detected_image_nums = len(detetced_image_list)

print(detected_image_nums)

print(detetced_image_list)