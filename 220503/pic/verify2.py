from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from glob import glob

labels_path = r'220503\pic\converted_keras\labels.txt'
image_list = glob(r'220503\pic\검증\*.jpg')
image_list.extend(glob(r'220503\pic\검증\*.png'))

model = load_model(r'220503\pic\converted_keras\keras_model.h5')

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

for image_path in image_list:
    image = Image.open(image_path)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    
    prediction = model.predict(data)
    print(prediction)
    
    with open(labels_path, 'rt', encoding='UTF-8') as f:
        readLines = f.readlines()
        
    if prediction[0, 0] > prediction[0, 1]:
        print(image_path, readLines[0])
    else:
        print(image_path, readLines[1])