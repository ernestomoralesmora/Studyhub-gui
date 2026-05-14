#!/bin/bash
set -euo pipefail
source /home/ernesto_7/Escritorio/studyhub-gui/parts/copy-files/run/environment.sh
set -x
cp --archive --link --no-dereference . "/home/ernesto_7/Escritorio/studyhub-gui/parts/copy-files/install"
