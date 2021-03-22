import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np


def importarImagen(ruta):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)
    # Load the model
    model = tensorflow.keras.models.load_model('keras_model.h5')
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    image = Image.open(ruta)

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)

    for i in prediction:
        if i[0] > 0.8:
            resultado = "Mamifero"
            return resultado
        elif i[1] > 0.8:
            resultado = "Ave"
            return resultado
        elif i[2] > 0.8:
            resultado = "Reptil"
            return resultado
        elif i[3] > 0.8:
            resultado = "Pez"
            return resultado
        else:
            resultado = "no se logro identificar una especie para esta imagen"
            return resultado

