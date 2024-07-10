#!/bin/bash

PROTO_DIR="./proto"
OUT_DIR="./server"

mkdir -p ${OUT_DIR}

for proto_file in ${PROTO_DIR}/*.proto; do
  poetry run python -m grpc_tools.protoc -I${PROTO_DIR} --python_out=${OUT_DIR} --grpc_python_out=${OUT_DIR} ${proto_file}
done
