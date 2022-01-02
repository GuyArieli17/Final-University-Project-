# how to build
docker build -t pong:latest -f network/machine-learning/Dockerfile .
docker build -t simulation:latest -f network/simulator/Dockerfile .
# Let's run
docker run -i --net=host pong:latest
docker run -i --net=host simulator:latest