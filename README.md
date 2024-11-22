# microns-morphology
Modules and Schemas for Morphological Processing of EM Datasets

# Installation Instructions

This repository includes two Python packages: API and Development. 

The Development package includes a pre-configured Docker container with all necessary dependencies, including Python.

To install the API:

```
pip install git+https://github.com/cajal/microns-morphology.git#subdirectory=python/microns-morphology-api
```

To run the development environment:

After cloning this repo, create a .env file inside the deploy folder. Even if you don’t specify any variables, an empty .env file is required for Docker Compose to function correctly. You can include the following optional variables:

```
DJ_HOST: Optional - MySQL database host for using DataJoint  
DJ_USER: Optional - DataJoint username  
DJ_PASS: Optional - DataJoint password  
JUPYTER_PORT_CONTAINER: Optional - Desired port for accessing JupyterLab (defaults to 8888)  
JUPYTER_PASSWORD: Optional - Password for JupyterLab (defaults to no password)  
GITHUB_TOKEN: Optional - GitHub token for cloning private repositories  
```

Ensure Docker is installed and running on your system. Then run:

```
docker compose build notebook
```
The build can take several minutes. Once complete run:  
```
docker compose up -d notebook
```
The -d flag runs the container in detached mode, allowing it to run in the background.

Navigate to https://localhost:8888 in your browser. If you specified a custom port in your .env file, replace 8888 with that port.