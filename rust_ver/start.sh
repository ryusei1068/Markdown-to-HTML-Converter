#!/bin/bash

docker build -t file_converter_rs .
docker run -it --name file_converter_rs file_converter_rs:latest
