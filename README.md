Container Management SaaS (Flask + Docker)

PROJECT DESCRIPTION
This project is a SaaS web application that provides a web interface for managing Docker containers.
Users can create, start, stop, delete, and view the status of Nginx containers running with a custom index.html page.

This application is designed to run ONLY on Linux systems (Ubuntu, Rocky Linux, etc.).
Docker on Windows is NOT used.

--------------------------------------------------

FEATURES
- Create Docker containers from a web interface
- Run Nginx containers with a custom HTML page
- Start containers
- Stop containers
- Delete containers
- View container status (running / stopped)
- Manage containers using Docker CLI through a Python backend

--------------------------------------------------

TECHNOLOGIES USED
Backend: Python (Flask)
Frontend: HTML, CSS
Container Runtime: Docker
Web Server: Nginx
Operating System: Linux (Ubuntu )
Version Control: Git & GitHub

--------------------------------------------------

PROJECT STRUCTURE

projet-python/
|-- app.py
|-- requirements.txt
|-- README.txt
|-- templates/
   |-- index.html
|-- static/
   |-- style.css
|-- nginx/
   |-- index.html

--------------------------------------------------

PREREQUISITES
The following must be installed on the Linux vm:
- Python 3
- Docker Engine
- Git

Installation commands:
sudo apt update
sudo apt install -y docker.io python3 python3-pip git

--------------------------------------------------

DOCKER CONFIGURATION
Add the user to the Docker group:
sudo usermod -aG docker $USER

Apply group changes:
newgrp docker

Verify Docker access:
docker ps

--------------------------------------------------

HOW TO RUN THE PROJECT

1. Clone the repository:
git clone https://github.com/Aziz-Chaabi/container-saas.git
cd projet-python

2. Install Python dependencies:
pip3 install -r requirements.txt

3. Start the Flask application:
python3 app.py

The application will run on:
http://<VM-IP>:5000

--------------------------------------------------

USING THE WEB INTERFACE
From the web interface, the user can:
- Enter a container name
- Enter a unique port number (example: 8081, 8082)
- Create a container
- Start, Stop, or Delete containers

Access a container in the browser:
http://<VM-IP>:<PORT>

A custom Nginx page will be displayed (not the default page).

--------------------------------------------------

EXAMPLE
Container Name: nginx1  | Port: 8081
Container Name: nginx2  | Port: 8082

--------------------------------------------------

ARCHITECTURE

Browser
   |
   v
Flask Web Application
   |
   v
Docker CLI (Python subprocess)
   |
   v
Docker Engine
   |
   v
Nginx Containers

--------------------------------------------------

LIMITATIONS
- No authentication implemented
- Flask development server only
- Ports must be unique per container
- Docker commands are executed using Docker CLI

--------------------------------------------------

This project demonstrates:
- SaaS application architecture
- Docker container lifecycle management
- Linux permissions and Docker groups
- Integration between backend and containers

--------------------------------------------------


