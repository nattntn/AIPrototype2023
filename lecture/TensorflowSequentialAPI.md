# การสร้าง Neural Network ด้วย Tensorflow Sequential API 
1. Sequential (ง่าย แต่สร้างได้แต่แบบไม่ซับซ้อน (วิ่งได้เเต่แบบเส้นตรง))
2. Functional (ยากขึ้นมาอีกนิด แต่สามารถปรับเส้นทาง ให้มีความซับซ้อนได้)
3. Subclassing (ยากสุด แต่สามารถแก้ไขได้ตามที่เราต้องการ)

# Sequential
## Import
```
import tensorflow as tf # run
from tensorflow import keras #API / UI
from tensorflow.keras import layers
```
## Define type 1 
```
# Define Sequential model witn 3 layers
model = keras.Sequential(
    [
     keras.Input(shape=(4,)),
     layers.Dense(2, activation="relu",name="layer1"),
     layers.Dense(3, activation="relu",name="layer2"),
     layers.Dense(5, activation="softmax",name="output")
    ]
)
```
## Define type 2
```
model2 = keras.Sequential()
model2.add(keras.Input(shape=(4,)))
model2.add(layers.Dense(2, activation="relu"))
model2.add(layers.Dense(3, activation="relu"))
model2.add(layers.Dense(5, activation="softmax"))
```

# Functional
## Import
``` 
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
```
## create model
```
input_images = keras.Input(shape=(32, 32, 3), name="img") # input shape shape=(32, 32, 3)
model = layers.Conv2D(32, (3, 3), activation="relu", name="conv1")(input_images) # (input_images) input จาก output  layer ก่อนหน้า
model = layers.MaxPooling2D((2, 2), name="maxpool1")(model)
model = layers.Conv2D(64, (3, 3), activation='relu', name="conv2")(model)
model = layers.MaxPooling2D((2, 2), name="maxpool2")(model)
model = layers.Conv2D(64, (3, 3), activation='relu', name="conv3")(model)
model = layers.Flatten(name="Flatten")(model)
model = layers.Dense(64, activation='relu', name="activation")(model)
output = layers.Dense(10, name="output")(model)

my_model = keras.Model(input_images, output, name = "mymodel")
```

# ResNet
มี skip connection
```
inputs = keras.Input(shape=(32, 32, 3), name="img")
x = layers.Conv2D(32, 3, activation="relu")(inputs)
x = layers.Conv2D(64, 3, activation="relu")(x)
block_1_output = layers.MaxPooling2D(3)(x)

x = layers.Conv2D(64, 3, activation="relu", padding="same")(block_1_output)
x = layers.Conv2D(64, 3, activation="relu", padding="same")(x)
block_2_output = layers.add([x, block_1_output]) # รับ output ทั้งแบบปกติ และ ที่เป็น skip connection

x = layers.Conv2D(64, 3, activation="relu", padding="same")(block_2_output)
x = layers.Conv2D(64, 3, activation="relu", padding="same")(x)
block_3_output = layers.add([x, block_2_output])

x = layers.Conv2D(64, 3, activation="relu")(block_3_output)
x = layers.GlobalAveragePooling2D()(x) # sum ออกมาเป็นเส้นยาวๆ
x = layers.Dense(256, activation="relu")(x)
x = layers.Dropout(0.5)(x)
outputs = layers.Dense(10)(x)

resnet_model = keras.Model(inputs, outputs, name="toy_resnet")
resnet_model.summary()
```

# Tensorflow Data Pipeline  
- [data augmentation](https://machinelearningmastery.com/how-to-configure-image-data-augmentation-when-training-deep-learning-neural-networks/)
- ระบุ path
  - 1. flow_from_directory
  - 2. flow_from_dataframe
