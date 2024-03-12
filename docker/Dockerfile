FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt update \
    && apt install -y \
    locales \
    gcc \
    g++ \
    build-essential \
    python3-pip \
    python3 \
    neovim \
    vim \
    nano \
    net-tools \
    tmux \
    inetutils-ping \
    software-properties-common \
    curl \
    htop

RUN locale-gen en_US en_US.UTF-8 \
    && update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

RUN add-apt-repository universe \
    && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null 

RUN apt update \
    &&  apt install -y \
    ros-dev-tools \
    ros-iron-desktop

RUN sudo apt update && sudo apt install espeak ffmpeg libespeak1 -y
RUN pip install ollama

