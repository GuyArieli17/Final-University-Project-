#!/bin/bash

docker_image_name=simulation
docker_container_name=test
#If image exist delete it
if [[ "$(docker images -q $docker_image_name 2> /dev/null)" != "" ]]; then
    echo "DELETEING EXISTING IMAGE ..."
    docker rmi simulation    
    echo
    echo "____________________________"
    echo
fi

echo
echo "Creating Simulation Image ..."
echo
# Create a new image
docker build -t simulation . 
echo
echo "____________________________"
echo

echo "Run container from simulation image"
docker run --name $docker_container_name -d simulation
echo


echo "Copy replay file and paste in ./container-output"
docker cp test:/usr/python-code/simulation/replay/replay.txt ./container-output
echo

echo "Copy roadnet file and paste in ./container-output"
docker cp test:/usr/python-code/simulation/replay/roadnet.json ./container-output
echo

echo "Remove Container"
docker rm $docker_container_name
echo


echo "EXIT PROGRAM PRESS KEY"
while [ true ] ; do
    read -t 3 -n 1
    if [ $? = 0 ] ; then
        exit ;
    else
        echo "End Task"
    fi
done