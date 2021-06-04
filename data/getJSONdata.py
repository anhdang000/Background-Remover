import json
import os
from os.path import join
import sys
from tqdm import tqdm
import cv2
import numpy as np

OUTPUT_FILE_PATH = 'data/init.json'
DATA_DIR = 'data/database'

IMG_IDS = os.listdir(DATA_DIR)
IMG_IDS.sort()
IMG_PATHS = [join(DATA_DIR,img_id) for img_id in IMG_IDS]

data = []
for i, (img_id, img_path) in tqdm(enumerate(zip(IMG_IDS, IMG_PATHS))):
    try:
        img = cv2.imread(img_path)
        is_valid = True
        h , w = img.shape[0], img.shape[1]
    except:
        is_valid = False
        h, w = None, None

    
    entry = {}
    entry["id"] = img_id
    entry["path"] = img_path
    entry["is_valid"] = is_valid
    entry["width"] = w
    entry["height"] = h

    data.append(entry)

with open(OUTPUT_FILE_PATH, 'w') as outputfile:
    json.dump(data, outputfile)

