#!/bin/bash
set -euo pipefail
source /home/ernesto_7/Escritorio/studyhub-gui/parts/gnome/sdk/run/environment.sh
set -x
make -j"16" GPU_WRAPPER=gpu-2404-wrapper
make -j"16" install GPU_WRAPPER=gpu-2404-wrapper DESTDIR="/home/ernesto_7/Escritorio/studyhub-gui/parts/gnome/sdk/install"
