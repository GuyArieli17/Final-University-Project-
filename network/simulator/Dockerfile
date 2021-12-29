FROM python:3.8-alpine

# copy rmr libraries from builder image in lieu of an Alpine package
COPY --from=nexus3.o-ran-sc.org:10002/o-ran-sc/bldr-alpine3-rmr:4.0.5 /usr/local/lib64/librmr* /usr/local/lib64/

# RMR setup
RUN mkdir -p /opt/route/
COPY test_route.rt /opt/route/test_route.rt
ENV LD_LIBRARY_PATH /usr/local/lib/:/usr/local/lib64
ENV RMR_SEED_RT /opt/route/test_route.rt

# sdl needs gcc
RUN apk update && apk add gcc musl-dev bash

# Install.
RUN pip3 install ricxappframe==1.3.0
COPY simulator/ping_xapp.py .

# Run
ENV PYTHONUNBUFFERED 1
CMD python ping_xapp.py
