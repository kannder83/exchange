FROM python:3.9

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN python3.9 -m pip install --no-cache-dir -r requirements.txt
COPY . .
CMD python3.9 main.py