FROM ubuntu:22.04

WORKDIR /file-converter
RUN apt update && apt install -y python3
RUN apt install -y python3-pip && pip install markdown
RUN chmod 777 /file-converter
RUN groupadd Recursion && useradd recursionist -G Recursion

COPY python_ver/file_converter.py/ /file-converter/
COPY README.md /file-converter/
USER recursionist
