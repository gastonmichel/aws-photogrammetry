#!/bin/bash

/data/Meshroom-2019.1.0/meshroom_photogrammetry --input `pwd`/input --output `pwd`/output --save project.mg

/data/Meshroom-2019.1.0/meshroom_compute project.mg --toNode Publish_1 --forceStatus
cd /home
shutdown -h now

