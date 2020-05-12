import requests
from bs4 import BeautifulSoup
import cv2
from PIL import Image
import uuid
import imageio
import numpy as np
from os import walk
import re
from os import path
import subprocess
import os

def preprocess(fp):
    gif = imageio.get_reader(fp)
    im = np.reshape(gif.get_data(0), (40, 135, 4))[:, :, 0:3]
    h, w, c = im.shape
    for i in range(h):
        for j in range(67):
            px = im[i][j]
            if (np.all(px == [153, 128, 204]) or np.all(px == [51, 0, 51]) or np.all(px == [102, 85, 102]) or np.all(
                    px == [102, 43, 204]) or np.all(px == [51, 0, 0]) or np.all(px == [51, 0, 204]) or np.all(
                    px == [0, 43, 204])
                    or np.all(px == [0, 0, 204]) or np.all(px == [0, 0, 255]) or np.all(px == [0, 0, 0]) or np.all(
                        px == [0, 85, 204]) or np.all(px == [51, 0, 153]) or np.all(px == [0, 0, 51]) or np.all(
                        px == [0, 0, 153])
                    or np.all(px == [0, 0, 102]) or np.all(px == [51, 0, 102]) or np.all(px == [51, 43, 204]) or np.all(
                        px == [51, 43, 102]) or np.all(px == [51, 43, 153]) or np.all(px == [51, 0, 255]) or np.all(
                        px == [51, 43, 51])):
                im[i][j] = [0, 0, 0]
                pass
            else:
                im[i][j] = [255, 255, 255]
        for j in range(67, 135):
            px = im[i][j]
            if (np.all(px == [153, 43, 102]) or np.all(px == [102, 43, 51]) or np.all(
                    px == [102, 43, 102]) or np.all(px == [51, 0, 102]) or np.all(px == [51, 0, 0]) or np.all(
                    px == [102, 0, 102]) or np.all(px == [0, 0, 51]) or
                    np.all(px == [102, 43, 153]) or np.all(px == [51, 0, 51]) or np.all(
                        px == [51, 43, 153]) or np.all(px == [51, 0, 153]) or np.all(px == [102, 0, 51]) or np.all(
                        px == [0, 0, 102]) or np.all(px == [102, 0, 153]) or
                    np.all(px == [102, 0, 0]) or np.all(px == [0, 0, 0]) or np.all(px == [51, 43, 102]) or np.all(
                        px == [0, 0, 153])):
                im[i][j] = [0, 0, 0]
                pass
            else:
                im[i][j] = [255, 255, 255]
    im[:, 0:16, :] = [255, 255, 255]
    im[:, 119:, :] = [255, 255, 255]
    im[35:40, :, :] = [255, 255, 255]
    cvim = cv2.cvtColor(im.astype(np.uint8),cv2.COLOR_RGB2GRAY)
    #cvim = cv2.morphologyEx(cvim, cv2.MORPH_CLOSE, (1,1))
    #im = Image.fromarray(im)
    label = fp.split('\.')[0].split('_')[1]
    resfp = path.join(dest_dir, uuid.uuid4().hex + '_' + label + '.jpg')
    #im.save(resfp, 'jpeg')
    cv2.imwrite(resfp, cvim)
    return path.join(os.getcwd(),resfp)

source_dir = 'iiimmmsss'
dest_dir = 'processres'

f = []
for (dirpath, dirnames, filenames) in walk(source_dir):
    f.extend(filenames)
    break

cc=0
corr=0
for p in f:
    cc+=1;
    truth = p.split('.')[0].split('_')[1].upper()
    pp = path.join(source_dir,p)
    resfp = preprocess(pp)
    proc = subprocess.Popen(["tesseract",resfp,"out"], cwd="C:\Program Files (x86)\Tesseract-OCR", stdout=subprocess.PIPE)
    proc.communicate()
    with open("C:\Program Files (x86)\Tesseract-OCR\out.txt", 'r') as file:
        pred = re.sub(r'[^a-zA-Z0-9]','', file.read()).upper()
        print(truth, pred)
        if truth==pred:
            corr+=1
print('正确率:'+str(corr/cc))

















# gif = imageio.get_reader('1582254844542.gif')
# im = np.reshape(gif.get_data(0),(40,135,4))[:,:,0:3]
# h,w,c = im.shape
# for i in range(h):
#     for j in range(67):
#         px = im[i][j]
#         if (np.all(px==[153,128,204]) or np.all(px==[51,0,51]) or np.all(px==[102,85,102]) or np.all(px==[102,43,204]) or np.all(px==[51,0,0]) or np.all(px==[51,0,204]) or np.all(px==[0,43,204])
#                 or np.all(px==[0,0,204]) or np.all(px==[0,0,255]) or np.all(px==[0,0,0]) or np.all(px==[0,85,204]) or np.all(px==[51,0,153]) or np.all(px==[0,0,51]) or np.all(px==[0,0,153])
#                 or np.all(px == [0, 0, 102]) or np.all(px==[51,0,102]) or np.all(px==[51,43,204]) or np.all(px==[51,43,102]) or np.all(px==[51,43,153]) or np.all(px==[51,0,255]) or np.all(px==[51,43,51])):
#             im[i][j] = [0, 0, 0]
#             pass
#         else:
#             im[i][j] = [255,255,255]
# for i in range(h):
#     for j in range(67,135):
#         px = im[i][j]
#         if (np.all(px==[153,43,102]) or np.all(px==[102,43,51]) or np.all(px==[102,43,102]) or np.all(px==[51,0,102]) or np.all(px==[51,0,0]) or np.all(px==[102,0,102]) or np.all(px==[0,0,51]) or
#                 np.all(px ==[102, 43, 153]) or np.all(px==[51,0,51]) or np.all(px==[51,43,153]) or np.all(px==[51,0,153]) or np.all(px==[102,0,51]) or np.all(px==[0,0,102]) or np.all(px==[102,0,153]) or
#                 np.all(px == [102, 0, 0]) or np.all(px==[0,0,0]) or np.all(px==[51,43,102]) or np.all(px==[0,0,153])):
#             im[i][j] = [0, 0, 0]
#             pass
#         else:
#             im[i][j] = [255,255,255]
#
# im = Image.fromarray(im)
# im.save('out.jpg')
#im.show()

# for i in im.shape
# im[:, :, 2][im[:, :, 2]<40] = 255
# thresh,im = cv2.threshold(im, 200, 255, cv2.THRESH_BINARY)
# cv2.imwrite('01.jpg',im)



# if ((px[0] == 0 or px[0] == 51 or px[0] == 102) and (px[1] == 0 or px[1] == 43) and (
#         px[2] == 0 or px[2] == 51 or px[2] == 102 or px[2] == 153 or px[2] == 204 or px[2] == 255)) \
#         and not (px[1] == 43 and (px[2] == 204)) \
#         and not (px[0] == 51 and (px[2] == 51 or px[2] == 102)):
#     # im[i][j] = [0, 0, 0]
#     pass
# else:
#     im[i][j] = [255, 255, 255]