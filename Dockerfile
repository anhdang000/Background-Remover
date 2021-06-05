FROM nvidia/cuda:10.2-base

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update

RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 
RUN conda --version

ADD . /bgrm_DeepLabV2
WORKDIR /bgrm_DeepLabV2

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
