# StudyHub Task Manager

StudyHub Task Manager is a desktop task management application developed in Python using Tkinter.

The application allows users to create, organize, and manage daily tasks through a simple graphical interface with priority levels and completion tracking.

This project was developed as part of an Erasmus university assignment related to Operating Systems, Docker containerization, Snap packaging, and Ubuntu Core integration.

---

# Features

- Add tasks with priority levels:
  - High
  - Medium
  - Low

- Mark tasks as completed or undo completion
- Delete tasks
- Automatic task persistence using JSON
- Dynamic task counters
- Scrollable task list
- Priority-based color system:
  - 🔴 High
  - 🟠 Medium
  - 🟢 Low
- User-friendly graphical interface
- Automatic task sorting by priority

---

# Application Preview

![Application Screenshot](screenshots/screenshot.png)

---

# Project Structure

```text
studyhub-gui/
│
├── app/
│   ├── main.py
│   ├── task_manager.py
│   ├── storage.py
│   └── data/
│       └── tasks.json
│
├── screenshots/
│   └── screenshot.png
│
├── snap/
│   └── snapcraft.yaml
│
├── ubuntu-core/
│   ├── build-image.sh
│   ├── studyhub-rpi5.model
│   └── README.md
│
├── Dockerfile
├── launcher.sh
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Technologies Used

- Python 3
- Tkinter
- JSON
- Docker
- Snapcraft
- Ubuntu Core

---

# Requirements

Make sure Python 3 is installed on your system.

Install Tkinter on Ubuntu/Linux:

```bash
sudo apt install python3-tk
```

---

# Running the Application

Navigate to the application folder:

```bash
cd studyhub-gui/app
```

Run the application:

```bash
python3 main.py
```

---

# How the Application Works

- Tasks are stored locally in a JSON file (`tasks.json`)
- Each task contains:
  - Task text
  - Priority
  - Completion status

- The interface updates dynamically after each action
- Tasks are automatically sorted by priority:
  - High → Medium → Low

---

# Docker Support

The application can also run inside a Docker container.

## Build the Docker image

```bash
docker build -t studyhub-gui .
```

## Allow local graphical access

```bash
xhost +local:
```

## Run the Docker container

```bash
docker run -it \
  --rm \
  --net=host \
  -e DISPLAY=$DISPLAY \
  -e XAUTHORITY=$XAUTHORITY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v $XAUTHORITY:$XAUTHORITY \
  -v $(pwd)/app/data:/app/data \
  studyhub-gui
```

This configuration allows the Tkinter graphical interface to be displayed from inside the Docker container while preserving task data locally.

---

# Snap Packaging

The project includes Snap packaging support.

## Build the Snap package

```bash
snapcraft pack
```

In some environments, network and permission restrictions required the use of:

```bash
sudo snapcraft pack --destructive-mode
```

## Install the Snap package

```bash
sudo snap install studyhub-gui_1.0_amd64.snap --devmode
```

## Run the Snap application

```bash
snap run studyhub-gui
```

---

# Ubuntu Core Integration

The repository also contains a prepared Ubuntu Core integration structure for Raspberry Pi 5.

## Included files

- `studyhub-rpi5.model`
- `build-image.sh`
- `README.md`

## Purpose

The integration structure prepares the project for deployment on Ubuntu Core devices using Snap packages.

At this stage, generating the final Ubuntu Core image requires:

- A signed model assertion
- An ARM64 Snap package
- Raspberry Pi 5 hardware testing

The structure and workflow were implemented following the Ubuntu Core documentation and deployment process.

---

# Author

Ernesto Morales Mora


