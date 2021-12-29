# how to build
docker build -t ping:latest -f machine-learning/Dockerfile .
docker build -t ping:latest -f simulator/Dockerfile .
# Let's run
docker run -i --net=host ping:latest
docker run -i --net=host pong:latest