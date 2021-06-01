import os
import sys
import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from omegaconf import OmegaConf

from libs.models import *
from libs.utils import DenseCRF

from demo import get_device, get_classtable, setup_postprocessor


# Configurations
MODEL_PATH = 'deeplabv2_resnet101_msc-cocostuff164k-100000.pth'
CONFIG_PATH = 'configs/cocostuff164k.yaml'
CRF = False
CUDA = True

INPUT_SIZE = 500
IMAGE_SIZE_LIMIT = 10000000


# Setup
CONFIG = OmegaConf.load(CONFIG_PATH)
device = get_device(CUDA)
torch.set_grad_enabled(False)

classes = get_classtable(CONFIG)
postprocessor = setup_postprocessor(CONFIG) if CRF else None

model = eval(CONFIG.MODEL.NAME)(n_classes=CONFIG.DATASET.N_CLASSES)
state_dict = torch.load(MODEL_PATH, map_location=lambda storage, loc: storage)
model.load_state_dict(state_dict)
model.eval()
model.to(device)
print("Model:", CONFIG.MODEL.NAME)

classes_of_interest = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 
    'boat', 'traffic light', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 
    'bear', 'zebra', 'giraffe', 'hat', 'backpack', 'umbrella', 'handbag', 'suitcase'
    ]

def preprocessing(image, device, CONFIG):
    # Calculate scales
    h, w, _ = image.shape
    scale_factor = [INPUT_SIZE/max(w, h), INPUT_SIZE/max(w, h)]
    newW = w * scale_factor[0]
    newH = h * scale_factor[1]
    
    # Refine scales
    while newW < 50:
        scale_factor[0] *= 2
        newW = w * scale_factor[0]
    while newH < 50:
        scale_factor[1] *= 2
        newH = h * scale_factor[1]

    image = cv2.resize(image, dsize=None, fx=scale_factor[0], fy=scale_factor[1])
    raw_image = image.astype(np.uint8)

    # Subtract mean values
    image = image.astype(np.float32)
    image -= np.array(
        [
            float(CONFIG.IMAGE.MEAN.B),
            float(CONFIG.IMAGE.MEAN.G),
            float(CONFIG.IMAGE.MEAN.R),
        ]
    )

    # Convert to torch.Tensor and add "batch" axis
    image = torch.from_numpy(image.transpose(2, 0, 1)).float().unsqueeze(0)
    image = image.to(device)

    return image, raw_image
