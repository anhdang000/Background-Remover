# TRAINING - Deployment Instruction [Week 1]

Author: Dang Linh Anh

Update: 03/06/2021

Source codes for DeepLab model are from the original repository: https://github.com/kazuto1011/deeplab-pytorch
## Branches:

- Master

## Dependencies:

- Python >= 3.6
- Pytorch > 1.2.0
- Torchvision
- FastAPI
- Uvicorn


## Deploy instructions: 

- Step 1: Clone the repository.

```sh
# Clone the repo
git clone https://gitlab.com/eyeq-training/anh-dang-training/anh-dang-first-week/
cd anh-dang-first-week
```

- Step 2: Download the pretrained weights on COCO-Stuff 164k.

```sh
wget https://github.com/kazuto1011/deeplab-pytorch/releases/download/v1.0/deeplabv2_resnet101_msc-cocostuff164k-100000.pth
```
Other options are also available on the original repository. Please refer to the [Pretrained Weights Comparison](https://github.com/kazuto1011/deeplab-pytorch#performance). Weights file's path as well as config file's path should be reconfigured as `MODEL_PATH` and `CONFIG_PATH` in `model_configs.py` corresponding to the downloaded weights.

- Step 3: Required Python packages are listed in the Anaconda configuration file `configs/conda_env.yaml`. Please modify the listed `cudatoolkit=11.0` and `python=3.6` as needed and run the following commands.

```sh
# Set up with Anaconda
conda env create -f configs/conda_env.yaml
conda activate deeplab-pytorch
```

- Step 4: Initialize the server.

```sh
uvicorn server:app --host 0.0.0.0 --reload
```

- Step 5: The API is deployed on http://SERVER-IP:8000/challenge
