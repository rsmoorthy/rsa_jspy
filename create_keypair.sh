#!/bin/bash

if [[ -z $1 ]]; then
  echo "Usage: create_keypair.sh <keyname>"
  exit 1
fi

openssl genrsa -out $1.priv 2048
openssl rsa -in $1.priv -outform PEM -pubout -out $1.pub
