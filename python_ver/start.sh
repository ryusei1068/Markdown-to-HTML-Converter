#!/bin/bash

docker build -t file_converter_py .
docker run -it --name file_converter_py file_converter_py:latest