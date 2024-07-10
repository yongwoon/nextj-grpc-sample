#!/bin/bash

PROTO_DIR="./proto"
OUT_DIR="./src/proto"

mkdir -p ${OUT_DIR}

npx grpc_tools_node_protoc \
  --js_out=import_style=commonjs,binary:${OUT_DIR} \
  --grpc-web_out=import_style=typescript,mode=grpcwebtext:${OUT_DIR} \
  --proto_path=${PROTO_DIR} ${PROTO_DIR}/*.proto
