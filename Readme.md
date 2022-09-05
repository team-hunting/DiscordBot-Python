## Once this bot is running:
Use by replying to a message in discord and including the text "!insult" in your message. (no quotation marks needed)

## To run locally

- ```git clone ....```
- cd into directory
- python -m venv venv
- activate virtual environment ```.\venv\Scripts\activate```  (windows)
- pip install -r requirements.txt
- create .env file with contents: ```TOKEN = 'XXXXXXXXXXX'``` using your actual token from discord
- run with ```python bot.py```

## To run with docker-compose locally

- ```git clone ....```
- cd into directory
- modify Dockerfile: ```TOKEN = 'XXXXXXXXXXX'``` using your actual token from discord
- ```docker-compose build```
- ```docker-compose up -d```

## To run on DigitalOcean using docker-compose

- Spin up a droplet
- Go to 'Networking' and set up a firewall
- - Inbound Rules: ALL TCP, ALL UDP
- Attach firewall to your droplet
- SSH into droplet, or use 'Droplet Terminal' via UI (```ssh root@0.0.0.0``` using the ipv4 address of your droplet instead of 0.0.0.0)
- ```mkdir Discord```
- ```cd Discord```
- ```git clone ....```
- cd into newly created repository
- ```nano Dockerfile```
- Add your TOKEN (and uncomment ENV line):
- - ```ENV TOKEN=MT.....................k8O4``` (no quotation marks)
- Install docker on droplet: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04
- Install docker compose ```apt install docker-compose```
- ```docker-compose build```
- ```docker-compose up -d```
