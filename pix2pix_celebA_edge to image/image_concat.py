#from PIL import Image
import cv2
import numpy as np
import os

sketch_dir = '../hed/data/edge-results/hed_pretrained_bsds_multiscale/'
real_dir = '../StarGAN/data/CelebA_nocrop/images/'
output_dir = './datasets/train_data2/'

imgs_real = [i for i in os.listdir(real_dir) if '.jpg' in i]
imgs_sketch = [j for j in os.listdir(sketch_dir) if '.png' in j]

imgs_real.sort()
imgs_sketch.sort()
#print len(imgs_real),len(imgs_sketch)
nimgs = len(imgs_real)

for i in range(nimgs) :
    image_sketch = cv2.imread(sketch_dir + imgs_sketch[i])
    image_real = cv2.imread(real_dir + imgs_real[i])
    image_train = np.concatenate((image_real,image_sketch),axis=1)
    cv2.imwrite(output_dir+imgs_real[i],image_train)

