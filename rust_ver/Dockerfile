FROM rust:1.67

RUN USER=root cargo new --bin file_converter
WORKDIR /file_converter

COPY Cargo* ./
COPY ./src ./src
COPY README.md ./

RUN chmod 777 /file_converter
RUN groupadd Recursion && useradd recursionist -G Recursion
USER recursionist
