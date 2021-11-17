# echo "Pleas Enter Road Gird x,y"

echo "Build simulation image:"
docker build -t simulation .

echo "Run container from simulation image"
docker run --name test -d simulation

echo "Copy replay file and paste in ./container-output"
docker cp test:/usr/python-code/simulation/replay/replay.txt ./container-output

echo "Copy roadnet file and paste in ./container-output"
docker cp test:/usr/python-code/simulation/replay/roadnet.json ./container-output
