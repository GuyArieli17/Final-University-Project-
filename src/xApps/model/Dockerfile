# ==================================================================================
#   Copyright (c) 2020 Samsung Electronics Co., Ltd. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# ==================================================================================
FROM python:3.8

#RUN pip3 install torch

# copy rmr libraries from builder image in lieu of an Alpine package
COPY --from=nexus3.o-ran-sc.org:10002/o-ran-sc/bldr-alpine3-rmr:4.0.5 /usr/local/lib64/librmr* /usr/local/lib64/
# RMR setup
RUN mkdir -p /opt/route/
COPY init/test_route.rt /opt/route/test_route.rt
ENV LD_LIBRARY_PATH /usr/local/lib/:/usr/local/lib64
#ENV LIBRARY_PATH=/lib:/usr/lib
ENV RMR_SEED_RT /opt/route/test_route.rt

# sdl needs gcc
# python3 python3-dev
# RUN apk update && apk add py3-pip gcc musl-dev bash gfortran musl-dev zlib-dev jpeg-dev linux-headers g++ gcompat build-base wget openblas-dev libpng-dev freetype-dev gfortran
# linux-headers gcompat build-base
RUN apt-get update -y && apt-get install -y gcc musl-dev bash gfortran musl-dev zlib1g-dev libjpeg-dev g++ wget libopenblas-dev libpng-dev libfreetype6-dev gfortran build-essential
RUN ln -s /usr/lib/x86_64-linux-musl/libc.so /lib/libc.musl-x86_64.so.1


RUN pip install --upgrade pip

# Install
COPY setup.py /tmp
COPY README.md /tmp
COPY LICENSE.txt /tmp/
COPY src/ /tmp/src
COPY src/model_params.pth /opt/model/model_params.pth
COPY init/ /tmp/init

RUN pip install /tmp

RUN pip3 install numpy
# RUN pip3 install torch==1.10.1 -f https://download.pytorch.org/whl/cpu/torch_lts.html
RUN pip3 install torch==1.10.1 -f https://download.pytorch.org/whl/torch_lts.html

# Env - TODO- Configmap
ENV PYTHONUNBUFFERED 1
ENV CONFIG_FILE=/tmp/init/config-file.json

# For Default DB connection, modify for resp kubernetes env
ENV DBAAS_SERVICE_PORT=6379
ENV DBAAS_SERVICE_HOST=service-ricplt-dbaas-tcp.ricplt.svc.cluster.local

#Run
CMD run-hw-python.py
