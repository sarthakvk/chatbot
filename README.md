## Chatbot

### Steps to runserver
1. Run postgresql server and create database named chatbot, no password
2. localhost should be trust in pg_hba.conf for postgresql, so that localhost can connect to database without password
3. create virtual env and activete it.
4. run `python manage.py migrate`
5. then `python manage.py runserver`
6. Goto `localhost:8000/chat/bot`