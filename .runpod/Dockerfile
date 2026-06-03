FROM runpod/pytorch:2.8.0-py3.11-cuda12.8.1-cudnn-devel-ubuntu22.04
LABEL maintainer="E-Labs AI Studio" description="E-Labs Fine-Tune Worker"

ENV DEBIAN_FRONTEND=noninteractive PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1

ARG BASE_VOLUME="/runpod-volume"
ENV BASE_VOLUME=$BASE_VOLUME
ENV HF_DATASETS_CACHE="${BASE_VOLUME}/huggingface-cache/datasets"
ENV HUGGINGFACE_HUB_CACHE="${BASE_VOLUME}/huggingface-cache/hub"
ENV TRANSFORMERS_CACHE="${BASE_VOLUME}/huggingface-cache/hub"

COPY .runpod/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install --upgrade -r /tmp/requirements.txt

COPY .runpod/src /src
COPY handler.py /src/handler.py

WORKDIR /src
CMD ["python3", "/src/handler.py"]
