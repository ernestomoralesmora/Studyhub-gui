#!/bin/bash

MODEL_FILE="ubuntu-core/studyhub-rpi5.model"
SNAP_FILE="studyhub-gui_1.0_arm64.snap"

echo "Building Ubuntu Core image for Raspberry Pi 5..."
echo "Model file: $MODEL_FILE"
echo "Local snap: $SNAP_FILE"

ubuntu-image snap "$MODEL_FILE" --snap "$SNAP_FILE"