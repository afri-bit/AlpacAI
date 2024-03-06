# Setting up Development Environment with Docker

## Introduction

This documentation provides step-by-step instructions on how to use the provided Dockerfile and Docker Compose to set up a development environment for your project.

## Prerequsites

Before you begin, make sure you have the following installed on your machine:
* Docker
* Docker Compose

## Steps

### Step 1: Clone the Repository

Clone the project repository to your local machine using the following command:

```bash
git clone https://github.com/afri-bit/AlpacAI.git

# Change directory to the git project and to docker folder
cd AlpacAI/docker
```

### Step 2: Build the Docker Images

If you haven't downloaded the images or built the images on your PC run following command to build the images

```bash
docker compose build
```

### Step 3: Run the Kuksa Broker

```bash
docker compose run kuksa_server --insecure
```

You will see the following result after running it correctly

```bash
2024-03-06T23:10:18.640728Z  INFO databroker: Init logging from RUST_LOG (environment variable not found)
2024-03-06T23:10:18.640801Z  INFO databroker: Starting Kuksa Databroker 7d9d335486c7f361d6efb6e3f6f8f1b8625846e0
2024-03-06T23:10:18.641705Z  INFO databroker: Populating metadata from file 'vss_release_4.0.json'
2024-03-06T23:10:18.726078Z  WARN databroker: Authorization is not enabled.
2024-03-06T23:10:18.726449Z  INFO databroker::broker: Starting housekeeping task
2024-03-06T23:10:18.726511Z  INFO databroker::grpc::server: Listening on 0.0.0.0:55555
2024-03-06T23:10:18.726518Z  INFO databroker::grpc::server: TLS is not enabled
2024-03-06T23:10:18.726521Z  INFO databroker::grpc::server: Authorization is not enabled.
```

### Step 4: Run the Kuksa Client

Since the Kuksa broker docker container has internal network, that is created from the docker compose service, we need to know the container name in order to be able to connect to the Kuksa broker.  
To find the name of the container, open a new `Terminal` and type `docker ps`, and you will get

```bash
CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS   PORTS       NAMES
46660f81df32   ...                                  55555/tcp   docker-kuksa_server-run-4c965c41745d
```

The container name `docker-kuksa_server-run-4c965c41745d` will be generated dynamically after launching the `kuksa_server` container. This container name will be used to run the `kuksa_client` container.

To run the `kuksa_client` open a new `Terminal` and enter following command

```bash
docker compose run kuksa_client --server docker-kuksa_server-run-4c965c41745d:55555
```

If everything is set correctly, the following result will be shown in your terminal

```bash

  ⠀⠀⠀⢀⣤⣶⣾⣿⢸⣿⣿⣷⣶⣤⡀
  ⠀⠀⣴⣿⡿⠋⣿⣿⠀⠀⠀⠈⠙⢿⣿⣦⠀
  ⠀⣾⣿⠋⠀⠀⣿⣿⠀⠀⣶⣿⠀⠀⠙⣿⣷
  ⣸⣿⠇⠀⠀⠀⣿⣿⠠⣾⡿⠃⠀⠀⠀⠸⣿⣇⠀ ⣶⠀⣠⡶⠂⠀⣶⠀⠀⢰⡆⠀⢰⡆⢀⣴⠖⠀⢠⡶⠶⠶⡦⠀⠀⠀⣰⣶⡀
  ⣿⣿⠀⠀⠀⠀⠿⢿⣷⣦⡀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⢾⣏⠀⠀⠀⣿⠀⠀⢸⡇⠀⢸⡷⣿⡁⠀⠀⠘⠷⠶⠶⣦⠀⠀⢠⡟⠘⣷
  ⢹⣿⡆⠀⠀⠀⣿⣶⠈⢻⣿⡆⠀⠀⠀⢰⣿⡏⠀⠀⠿⠀⠙⠷⠄⠀⠙⠷⠶⠟⠁⠀⠸⠇⠈⠻⠦⠀⠐⠷⠶⠶⠟⠀⠠⠿⠁⠀⠹⠧
  ⠀⢿⣿⣄⠀⠀⣿⣿⠀⠀⠿⣿⠀⠀⣠⣿⡿
  ⠀⠀⠻⣿⣷⡄⣿⣿⠀⠀⠀⢀⣠⣾⣿⠟    databroker-cli
  ⠀⠀⠀⠈⠛⠇⢿⣿⣿⣿⣿⡿⠿⠛⠁     v0.4.1

Successfully connected to http://docker-kuksa_server-run-4c965c41745d:55555/
sdv.databroker.v1 > 
```

```bash
# Type help 
sdv.databroker.v1 > help

  connect [URI]            Connect to server
  get <PATH> [[PATH] ...]  Get signal value(s)
  set <PATH> <VALUE>       Set actuator signal
  subscribe <QUERY>        Subscribe to signals with QUERY, if you use kuksa feature comma separated list
  feed <PATH> <VALUE>      Publish signal value
  metadata [PATTERN]       Fetch metadata. Provide PATTERN to list metadata of signals matching pattern.
  token <TOKEN>            Use TOKEN as access token
  token-file <FILE>        Use content of FILE as access token
  help                     You're looking at it.
  quit                     Quit
```

With this, you are now able to communicate with the data broker to manipulate or read data.

### Step 5: Run the Core AlpacAI Container

> Assuming you are still inside the `docker` folder

Open a new `Terminal`

```bash
docker compose run alpacai
```