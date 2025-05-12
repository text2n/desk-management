# Occupancy management application

This project is a Occupancy management application that uses Langchain SQL agent and gemini 
for interacting using natural language. 

It includes a Docker setup for easy deployment and management.

## Project Structure

```
desk-management
├── app
│   └── main.py               # Entry point of the FastAPI application
├── storage
│   ├── app.log               # Application logs
│   └── db.sql                # SQL dump for setting up the MySQL database
├── docker-compose.yml        # Docker Compose configuration for services
├── Dockerfile                # Dockerfile for building the FastAPI application image
├── requirements.txt          # Dependencies for the FastAPI application
├── .env.example              # Sample .env file with environment variables
└── README.md                 # Project documentation
```

## Setup Instructions Docker

1. **Clone the repository:**
   ```
   git clone https://github.com/text2n/desk-management.git
   cd desk-managemnet
   ```
2. **Copy .env.example to .env and change configurations**
    ```
    cp .env.example .env
    
    Edit .env and change configurations
    ```
    For Docker deployment configure only GOOGLE_API_KEY

    For generating gemini api key refer this blog for steps 
    https://www.merge.dev/blog/gemini-api-key

3. **Build and run the application using Docker Compose:**
   ```
   sudo docker-compose up --build
   ```
   Please wait till application is started
3. **Access the application:**
   Open your browser and go to `http://localhost:8000`.

4. **For api documentation**
   Open your browser and go to `http://localhost:8000/docs`.


## Manual deployment instructions

Follow steps 1 & 2 from Docker

3. **Create virtual environment**
    ```
    python3 -m venv .venv
    ```
4. **Activate virtual environment**
    ```
    source .venv/bin/activate
    ```
5. **Install dependencies**
    ```
    pip install -r requirements.txt
    ```
6. **Run server**
    ```
    fastapi run app/main.py
    ```
7. **Access the application:**
   Open your browser and go to `http://localhost:8000`.


## Other helpful commands

### Update requirements (after installing new packages)
pip freeze > requirements.txt

### Deactivate virtualenv
deactivate

### Build docker container
sudo docker build -t fastapi-template .

### Run docker container
sudo docker run -d --name fastapicontainer -p 8000:8000 fastapi-template

### Build using docker compose
sudo docker compose build

### Run docker compose
sudo docker compose up -d

### Stop docker compose
sudo docker-compose down