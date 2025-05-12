## Clone git repo
git clone https://github.com/text2n/fastapi-template.git

## Create virtual environment
python3 -m venv .venv

## Activate virtual environment
source .venv/bin/activate

## Install dependencies
pip install -r requirements.txt

## Update requirements (after installing new packages)
pip freeze > requirements.txt

## Deactivate virtualenv
deactivate

## Copy .env.example to .env and change configurations
cp .env.example .env

## Run server
fastapi dev app/main.py

## Build docker container
docker build -t fastapi-template .

## Run docker container
docker run -d --name fastapicontainer -p 80:80 fastapi-template

## Build using docker compose
sudo docker-compose build

## Run docker compose
sudo docker-compose up -d

## Stop docker compose
sudo docker-compose down