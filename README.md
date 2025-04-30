# Docker Compose Examples

<p align="center">
  <a href="https://www.linkedin.com/in/abdullah-hendy-941071238/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://medium.com/@abdallahhendy15" target="_blank">
    <img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white" alt="Medium Badge"/>
  </a>
</p>

## Overview
This repository contains examples of using **Docker Compose** to run and manage multiple containers. This idea hits me as I faced a shortage of examples to practice on while I was learning. So, I built simple examples to **practice the idea** not more.

 ## 1. Python Flask + PostgreSQL DB
### 📚 Content
- This example contains a simple app with the Flask framework and attaches it to the PostgreSQL database.
- The `Dockerfile` file, which is used to write the configurations to build and run the container
    - The `.dockerignore` file specifies what Docker will ignore in building the app.
- The `docker-compose.yml` file to run and manage your **services**[containers] 
- The `.env.dev` file, which is used to specify your *Environment Variables*
    - Avoid writing it in the `docker-compose.yml` file for readability, simplicity, and security purposes.
    - I upload it for learning purposes, but in real life, **files that contain secrets are added to `.gitignore` and never made public**
 
 ### 🔧 Set Up:
 1. Clone the repo
 2. Run `docker compose up -d --build`  -> to build & run the app in detached mode.
 3. Visit http://localhost:5000 to see the content

### 📝 Some Notes
- Clone the repo (*now you've the app*)
    - Make your hands dirty and write the `Dockerfile` and `docker-compose.yml` files, then, return to the original project to check your knowledge <which'll be perfect Inshallah>
- Always keep the code files avoiding from other configuration files, such as `.env`, `Dockerfile`, etc.
- Mistakes are inevitable; learn from them and keep going. Try, try, try 💪
  
