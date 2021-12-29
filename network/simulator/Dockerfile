# FROM python:3.8-alpine
FROM python:3.8

# copy rmr libraries from builder image in lieu of an Alpine package
COPY --from=nexus3.o-ran-sc.org:10002/o-ran-sc/bldr-alpine3-rmr:4.0.5 /usr/local/lib64/librmr* /usr/local/lib64/

# RMR setup
RUN mkdir -p /opt/route/
COPY library .
COPY network/test_route.rt /opt/route/test_route.rt
ENV LD_LIBRARY_PATH /usr/local/lib/:/usr/local/lib64
ENV RMR_SEED_RT /opt/route/test_route.rt

# sdl needs gcc
RUN apt-get update -y && apt-get install -y gcc musl-dev bash gfortran musl-dev zlib1g-dev libjpeg-dev g++ wget libopenblas-dev libpng-dev libfreetype6-dev gfortran build-essential cmake
RUN ln -s /usr/lib/x86_64-linux-musl/libc.so /lib/libc.musl-x86_64.so.1

# Install.
# RUN pip install --upgrade pip
RUN pip3 install ricxappframe==1.3.0
RUN pip3 install gym
RUN pip3 install CityFlow/

COPY network/simulator/ping_xapp.py .

# Run
ENV PYTHONUNBUFFERED 1
CMD python ping_xapp.py
