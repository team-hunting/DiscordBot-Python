# syntax=docker/dockerfile:1

FROM python:3.9.2

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# ENV TOKEN=XXXXXXXXX

CMD [ "python3", "-m" , "bot.py"]