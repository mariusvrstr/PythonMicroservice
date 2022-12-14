# PythonMicroservice
Sample Microservice done in Python

![image](https://user-images.githubusercontent.com/2478826/196535978-7e386fc5-6319-4894-b2d0-b4566b43fe35.png)

## Setup Guide
1. Run the powershell script `.\setup.ps1` in the root of the folder (It will create a virtual env and install required packages)

## Stack Overview

### Overall
| Library        | Description | External Content                 |
|----------------|-------------|----------------------------------|
 | [sqlalchemy]() | ORM - DAL   | [Introduction]() > [Deep Dive]() |

### Scheduler
| Library     | Description               | External Content                 |
|-------------|---------------------------|----------------------------------|
 | [asyncio]() | Asyncronous Processessing | [Introduction]() > [Deep Dive]() |

### API Server
The swagger document can be found at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

| Library                                 | Description              | External Content                                                                                     |  
|-----------------------------------------|--------------------------|------------------------------------------------------------------------------------------------------|
 | [FastAPI](https://fastapi.tiangolo.com) | Design and document APIs | [Introduction](https://blog.devgenius.io/brief-introduction-to-fastapi-d6f25793b11a) > [Deep Dive]() |
 | [Uvicorn](https://www.uvicorn.org/)     | Web Server               | [Introduction]() > [Deep Dive]()                                                                     |

### Website
| Library                                              | Description         | External Content                 |
|------------------------------------------------------|---------------------|----------------------------------|
 | [Flask](https://flask.palletsprojects.com/en/2.2.x/) | Micro Web Framework | [Introduction]() > [Deep Dive]() |

### Testing
| Library                                               | Description              | External Content                                                                                                                               | 
|-------------------------------------------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
 | [Pytest](https://docs.pytest.org/en/7.1.x/index.html) | Python testing framework | [Introduction](https://docs.pytest.org/en/7.1.x/getting-started.html) > [Deep Dive](https://docs.pytest.org/en/7.1.x/reference/reference.html) |

## Included
- [X] Dependancy setup using requirements.txt
- [X] Rolling file logging with console output
- [X] Seperate application threads (API, Schedules, etc)
- [X] Asyncronous & Multi-Threaded Schedules
- [X] Swagger Documented API's (FastAPI)

## Feature Backlog
- [ ] Thread isolated logging
- [ ] Unit Testing
- [ ] Stress Testing (API Calls, Large Batches)
- [ ] ORM Data Access
- [ ] Proxy API Proxies (Request)
- [ ] Azure DevOps hosted on Linux container
- [ ] Database Migrations (CI/CD)
- [ ] Web System Health Page

