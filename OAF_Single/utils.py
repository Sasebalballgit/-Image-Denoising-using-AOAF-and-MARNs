import numpy as np
import imageio
import cv2
import os
from PIL import Image



def readfile(path):
    img_dir = sorted(os.listdir(path))
    all_folds = os.listdir(path)
    # image = 512 * 512 size 
    x = np.ones((len(all_folds), 512, 512), dtype=np.uint8)
    for i, file in enumerate(img_dir):
        if(file != 'desktop.ini'):
            img = Image.open(os.path.join(path, file))
            x[i] = img
    return x


def savefile(img, path_out, path_in):
    img_dir = sorted(os.listdir(path_in))
    for i, file in enumerate(img_dir):
        imageio.imwrite(os.path.join(path_out, 'out_'+file), img[i])
