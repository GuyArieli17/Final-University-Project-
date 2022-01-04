# how to build Guy
docker build -t drl:guy -f network/drl/Dockerfile .
docker build -t simulation:guy -f network/simulator/Dockerfile .
# Let's run From Guy
docker run -i --net=host drl:guy
docker run -i --net=host simulation:guy

# how to build Vlad
docker build -t pong:vlad -f network/drl/Dockerfile .
docker build -t simulation:vlad -f network/simulator/Dockerfile .
# Let's run From Vlad
docker run -i --net=host pong:vlad
docker run -i --net=host simulation:vlad

# how to build Eran
docker build -t pong:eran -f network/drl/Dockerfile .
docker build -t simulation:eran -f network/simulator/Dockerfile .
# Let's run From Eran
docker run -i --net=host pong:eran
docker run -i --net=host simulation:eran

# how to build Amit
docker build -t pong:amit -f network/drl/Dockerfile .
docker build -t simulation:amit -f network/simulator/Dockerfile .
# Let's run From Amit
docker run -i --net=host pong:amit
docker run -i --net=host simulation:amit