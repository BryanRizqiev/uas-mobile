from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np

def handle_uploaded_file(f):
    filepath = 'penyakitcabai/static/upload/'+f.name
    with open(filepath, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return filepath

def do_identification(model, path):
    img = image.load_img(path, target_size=(150,150), color_mode='rgba')

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])

    classes = model.predict(images, batch_size=10)

    if classes[0,1] != 0:
        return "leaf curl"
    elif classes[0,0] != 0:
        return "sehat"
    else:
        return "yellowwiss"
