# how to build Guy
docker build -t drl:guy -f network/drl/Dockerfile .
docker build -t simulation:guy -f network/simulator/Dockerfile .
# Let's run From Guy
docker run -i --net=host drl:guy
docker run -i --net=host simulation:guy

# how to build Vlad
docker build -t drl:vlad -f network/drl/Dockerfile .
docker build -t simulation:vlad -f network/simulator/Dockerfile .
# Let's run From Vlad
docker run -i --net=host drl:vlad
docker run -i --net=host simulation:vlad

# how to build Eran
docker build -t drl:eran -f network/drl/Dockerfile .
docker build -t simulation:eran -f network/simulator/Dockerfile .
# Let's run From Eran
docker run -i --net=host drl:eran
docker run -i --net=host simulation:eran

# how to build Amit
docker build -t drl:amit -f network/drl/Dockerfile .
docker build -t simulation:amit -f network/simulator/Dockerfile .
# Let's run From Amit
docker run -i --net=host drl:amit
docker run -i --net=host simulation:amit