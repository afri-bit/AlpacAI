FROM ubuntu:22.04

RUN apt update \
    && apt install -y \
        python3-pip \
        python3 \
        net-tools \
        tmux \
        inetutils-ping \
        software-properties-common

RUN add-apt-repository ppa:ecal/ecal-5.12 \
    && apt-get update \
    && apt-get install -y ecal python3-ecal5

RUN pip install kuksa-client