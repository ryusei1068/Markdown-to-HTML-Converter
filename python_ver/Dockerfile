FROM ubuntu:22.04

WORKDIR /file-converter
RUN apt update && apt install -y python3
RUN apt install -y python3-pip && pip install markdown
RUN chmod 777 /file-converter
RUN groupadd Recursion && useradd recursionist -G Recursion

COPY ./file_converter.py ./
COPY README.md ./
USER recursionist
