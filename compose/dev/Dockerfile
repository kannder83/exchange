FROM python:3.10.7
ENV PYTHONUNBUFFERED 1

# Update
# RUN apt-get update \ 
#     && apt-get -y install curl systemd cron vim && \ 
#     apt-get clean

# Filecrontab
# COPY root /var/spool/cron/crontabs/root

# Service
# RUN systemctl enable cron

# ENTRYPOINT ["cron", "-f"]

#Directory work
WORKDIR /usr/src/app

#Copy requirements files
COPY requirements.txt ./

# Install 
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# execute
# RUN chmod +x /usr/src/app/hello.py

# ENTRYPOINT ["crond", "-l", "2", "-f"]

# Excecute program
CMD python3 main.py