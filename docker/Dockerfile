FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

ENV USER_NAME=alpaca
ENV USER_PASSWORD=${USER_NAME}

# ========== Basic installation for ubuntu

RUN apt update \
    && apt install -y \
    locales \
    gcc \
    g++ \
    build-essential \
    python3 \
    python3-pip \
    neovim \
    vim \
    nano \
    net-tools \
    tmux \
    inetutils-ping \
    software-properties-common \
    curl \
    htop \
    git \
    libclang-dev 

RUN locale-gen en_US en_US.UTF-8 \
    && update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

RUN add-apt-repository universe \
    && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null 

RUN apt update \
    &&  apt install -y \
    ros-dev-tools \
    ros-iron-ros-base
    

# ========== User level

# Create a non-root user with sudo privileges
RUN useradd -m -s /bin/bash "${USER_NAME}" && \
    echo "${USER_NAME}:${USER_PASSWORD}" | chpasswd && \
    usermod -aG sudo "${USER_NAME}"

USER ${USER_NAME}

# Set the working directory
WORKDIR /home/${USER_NAME}

# Update the pip version
RUN pip install --upgrade pip


# Setup ROS environment
RUN echo 'source /opt/ros/iron/setup.sh' >> $HOME/.bashrc

# ========== RUST Things (with ROS2) - USER level

# Install rust 
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y \
    && echo 'source $HOME/.cargo/env' >> $HOME/.bashrc

RUN $HOME/.cargo/bin/cargo install cargo-ament-build  # --debug is faster to install

# Cargo for ROS2
RUN pip install git+https://github.com/colcon/colcon-cargo.git \
    && pip install git+https://github.com/colcon/colcon-ros-cargo.git

# Convagent Setup
RUN sudo apt update && sudo apt install espeak ffmpeg libespeak1 -y
RUN pip install ollama
