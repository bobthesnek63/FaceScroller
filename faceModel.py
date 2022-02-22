import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
from pynput.mouse import Controller

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

def learn():

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open('test_photo.jpg')

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    most = max(prediction[0])
    location = 0
    for i in range(len(prediction[0])):
        if prediction[0][i] == most:
            location = i

    print(prediction, location, most)


    mouse = Controller()
    if location == 0:
         mouse.scroll(0, 1)
    if location == 2:
         mouse.scroll(0, -1)


def resize(frame):
    width = 224
    height = 224
    dim = (width, height)
    return cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = resize(frame)
    cv2.imwrite('test_photo.jpg', frame)
    learn()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)