from python:3.9.6
RUN apt update && apt install --assume-yes build-essential libpq-dev python3-dev
ENV PYTHONUNBUFFERED=1 DB_HOST=postgres
COPY . /chatbot
WORKDIR /chatbot
RUN pip install -r requirements.txt

CMD ["sh", "start.sh"]