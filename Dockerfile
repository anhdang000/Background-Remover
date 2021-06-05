FROM continuumio/miniconda3:latest

WORKDIR /bgrm_DeepLabV2
ADD . /bgrm_DeepLabV2
 
# Download pretrained weights on COCO
RUN wget https://github.com/kazuto1011/deeplab-pytorch/releases/download/v1.0/deeplabv2_resnet101_msc-cocostuff164k-100000.pth

# Create conda environment
RUN conda env create -f configs/conda_env.yaml

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "deeplab-pytorch", "/bin/bash", "-c"]

# For opencv requirements
RUN apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6  -y

# Make sure that opencv is installed correctly
RUN python -c "import cv2"

ENTRYPOINT ["conda", "run", "-n", "deeplab-pytorch", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
