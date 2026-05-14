# Ubuntu Core Integration

This folder contains the files required to integrate the StudyHub GUI Snap package into an Ubuntu Core image for Raspberry Pi 5.

## Purpose

The goal is to create an Ubuntu Core image that includes the StudyHub Task Manager application as a Snap package.

## Files

- `studyhub-rpi5.model`: model assertion describing the Ubuntu Core image.
- `build-image.sh`: script showing how the image would be generated with `ubuntu-image`.

## Important Note

The current Snap package was built on an amd64 computer.  
For Raspberry Pi 5, the Snap must be built for `arm64`.

Example expected Snap file:

```bash
studyhub-gui_1.0_arm64.snap