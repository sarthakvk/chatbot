# Chatbot

## Live Demo
http://13.233.168.148/chat/bot/

## Steps to runserver with Docker
1. Install Docker and Docker Compose (https://docs.docker.com/compose/install/)
2. Docker should be running
3. In the project root run `docker-compose up`
4. Go to `localhost:8000` to view chatbot

## Runserver without Docker

### dependencies
1. Postgresql
2. Python >= 3.8


### Steps to runserver
1. Run postgresql server and create database named `chatbot`
2. edit `pg_hba.conf` to set `trust` method, so that we can connect to database without password ( I am not using authentication because whoever runs this code then should have same password for postgres user which might not be desirable.)
3. create virtual env and activate it.(`python -m venv venv && source venv/bin/activate`)
5. run `pip install -r requirements.txt` (if you face errors installing psycopg2 package look at this answer for clue https://stackoverflow.com/questions/5420789/how-to-install-psycopg2-with-pip-on-python)
4. run `python chatbot/manage.py migrate`
5. then `python chatbot/manage.py runserver`
6. Goto `localhost:8000/chat/bot`


> If you want to connect to postgresql database with password, then add database user password in the `DATABASE` dict in settings.py file  
> To avoid password edit pg_hba.conf(which is in data directory of postgresql), and set values to `trust`  
> sample pg_hba.conf is also added in this repository which you can checkout for your reference