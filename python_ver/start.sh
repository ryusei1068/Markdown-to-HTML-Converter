#!/bin/bash

docker build -t file_converter .
docker run -it --name file_converter file_converter:latest