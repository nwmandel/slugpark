#$ -S /bin/bash

# number of cars detected
./darknet detector test cfg/coco.data cfg/yolo.cfg yolo.weights data/WR2.jpg | grep car | wc -l

# number of motorbikes detected
./darknet detector test cfg/coco.data cfg/yolo.cfg yolo.weights data/WR2.jpg | grep motorbike | wc -l


