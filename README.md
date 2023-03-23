# Background Remover - Deployment Instruction

Author: Dang Linh Anh

Update: 03/06/2021

Source codes for DeepLab model are from the original repository: https://github.com/kazuto1011/deeplab-pytorch

# Table of contents
1. [Branches](#branches2)
2. [Dependencies](#dependencies2)
3. [Deploy instructions](#deploy2)


## 1. Branches: <a name="branches2"></a>
- Master
- Develop

## 2. Dependencies: <a name="dependencies2"></a>

- Python >= 3.6
- Pytorch > 1.2.0
- FastAPI
- Uvicorn
- Pymongo >= 3

# 3. Deploy Instruction: <a name="deploy2"></a>
- Step 1: Clone the repository.

```sh
# Clone the repo
git clone https://github.com/anhdang000/Background-Remover
cd Background-Remover
git checkout w2
```

- Step 2: Download the pretrained weights on COCO-Stuff 164k

```sh
wget https://github.com/kazuto1011/deeplab-pytorch/releases/download/v1.0/deeplabv2_resnet101_msc-cocostuff164k-100000.pth
```
Other options are also available on the original repository. Please refer to the [Pretrained Weights Comparison](https://github.com/kazuto1011/deeplab-pytorch#performance). Weights file's path as well as config file's path should be reconfigured as `MODEL_PATH` and `CONFIG_PATH` in `model_configs.py` corresponding to the downloaded weights.

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

- Step 6: The API is deployed on http://SERVER-IP:8888/challenge

- Step 7: To review stored data in MongoDB Database, have a check at http://SERVER-IP:8888/images
