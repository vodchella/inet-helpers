#!/bin/bash

ROOT_PATH=$(cd $(dirname $0) && pwd);
ln -s ${ROOT_PATH}/q.py /usr/bin/q
ln -s ${ROOT_PATH}/wiki.py /usr/bin/wiki