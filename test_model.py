import os
import PIL
import logging, os
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf
from tensorflow import keras
# import cv2
# import matplotlib.pyplot as plt
import numpy as np

img_path = 'mel.jpg' # измени на путь к своему изображению (вроде работает для png и jpg формата)
model = tf.keras.models.load_model('model-72.keras') # измени на свой путь к модели .keras

image = keras.utils.load_img(img_path, target_size=(224,224))
input_arr = keras.utils.img_to_array(image)
input_arr = np.array([input_arr])

pred = model.predict(input_arr)
pred2 = pred.tolist()[0]
diff = abs(pred2[0]-pred2[1])


classes = {0: 'melanoma', 1: 'nevus'}
cls = tf.argmax(pred, axis=1)
print(classes[int(cls)])