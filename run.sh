#!/bin/bash

docker_image_name=simulation
docker_container_name=test

#If container exist delete it
echo "DELETEING EXISTING CONTAINER ..."
docker container kill $docker_container_name || true
docker rm $docker_container_name || true

#If image exist delete it
echo "DELETEING EXISTING IMAGE ..."
docker rmi $docker_image_name || true
echo
echo "____________________________"
echo

echo
echo "Creating Simulation Image ..."
echo
# Create a new image
docker build -t $docker_image_name . 
echo
echo "____________________________"
echo

echo "Run container from simulation image"
docker run --name $docker_container_name -d simulation
echo

# cp -r container-output container-output-history/`date '+%Y-%m-%d-%H-%M-%S'`
# rm -r ./container-output/*
 echo "Copy files and paste in ./container-output"
# docker cp -a $docker_container_name:/usr/python-code/container-output/. ./container-output
# docker cp -a $docker_container_name:/usr/python-code/simulation/replay/. ./container-output
# echo


# echo "Remove Container"
# docker rm $docker_container_name
# echo

#
# echo "EXIT PROGRAM PRESS KEY"
# while [ true ] ; do
#     read -t 3 -n 1
#     if [ $? = 0 ] ; then
#         exit ;
#     else
#         echo "End Task"
#     fi
# done