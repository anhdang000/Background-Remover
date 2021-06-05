# TRAINING - Deployment Instruction

# Table of contents
1. [Week 1](#w1)
    1. [Branches](#branches1)
    2. [Dependencies](#dependencies1)
    3. [Deploy instructions](#deploy1)
2. [Week 2](#w2)
    1. [Branches](#branches2)
    2. [Dependencies](#dependencies2)
    3. [Deploy instructions](#deploy2)
3. [Week 3](#w3)

#  1. Week 1: <a name="w1"></a>

Author: Dang Linh Anh

Update: 03/06/2021

Source codes for DeepLab model are from the original repository: https://github.com/kazuto1011/deeplab-pytorch

## 1.1. Branches: <a name="branches1"></a>

- Master

## 1.2. Dependencies: <a name="dependencies1"></a>

- Python >= 3.6
- Pytorch > 1.2.0
- FastAPI
- Uvicorn


## 1.3. Deploy instructions: <a name="deploy1"></a>

- Step 1: Clone the repository.

```sh
# Clone the repo
git clone https://gitlab.com/eyeq-training/anh-dang-training/anh-dang-first-week/
cd anh-dang-first-week

# Switch to Week 1 version
git checkout w1
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


# 2. Week 2: <a name="w2"></a>

## 2.1. Branches: <a name="branches2"></a>
- Master
- Develop

## 2.2. Dependencies: <a name="dependencies2"></a>

- Python >= 3.6
- Pytorch > 1.2.0
- FastAPI
- Uvicorn
- Pymongo >= 3

# 2.3. Deploy Instruction: <a name="deploy2"></a>
- Step 1: Clone the repository.

```sh
# Clone the repo
git clone https://gitlab.com/eyeq-training/anh-dang-training/anh-dang-first-week/
cd anh-dang-first-week

# Switch to Week 2 version
git checkout w2
```

- Step 2: Download the pretrained weights on COCO-Stuff 164k as refered in <b>Week 1</b>

- Step 3: Download data to be stored in MongoDB Database

```sh
wget https://download1479.mediafire.com/zh0o43wv19jg/bfdomn0aazv86sl/data.zip
unzip images.zip -d data/
```

- Step 4: Generate JSON format data of the database

```sh
python data/getJSONdata.py
```
This script will create an JSON output file (`init.json`) located in `mongodb` folder

- Step 5: Run <b>Docker-compose</b> to create 2 docker container (named `fastapi` and `mongodb`)

```sh
docker-compose down && docker-compose build --no-cache && docker-compose up
```

- Step 6: The API for the computer vision challenge (regarded in <b>Week 1</b>) is deployed on http://SERVER-IP:8888/challenge

- Step 7: To review stored data in MongoDB Database, give a check at http://SERVER-IP:8888/images
