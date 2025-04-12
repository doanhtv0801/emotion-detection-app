from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint

# Đường dẫn dữ liệu
train_dir = './data/train'
val_dir = './data/test'

# Tạo generator cho ảnh grayscale 48x48
train_gen = ImageDataGenerator(rescale=1./255)
val_gen = ImageDataGenerator(rescale=1./255)

train_data = train_gen.flow_from_directory(train_dir, target_size=(48, 
48), color_mode='grayscale',
                                           batch_size=64, 
class_mode='categorical')
val_data = val_gen.flow_from_directory(val_dir, target_size=(48, 48), 
color_mode='grayscale',
                                       batch_size=64, 
class_mode='categorical')

# Mô hình CNN đơn giản
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 1)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(7, activation='softmax')  # FER2013 gồm 7 lớp
])

model.compile(optimizer='adam', loss='categorical_crossentropy', 
metrics=['accuracy'])

# Lưu model tốt nhất
checkpoint = ModelCheckpoint('model/emotion_model.h5', 
monitor='val_accuracy', save_best_only=True, mode='max')

# Huấn luyện mô hình
model.fit(train_data, validation_data=val_data, epochs=30, 
callbacks=[checkpoint])

