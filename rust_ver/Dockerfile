FROM rust:1.67

WORKDIR /file-converter
COPY Cargo* ./
COPY ./src ./src
COPY README.md /file-converter/

RUN chmod 777 /file-converter
RUN groupadd Recursion && useradd recursionist -G Recursion
USER recursionist
