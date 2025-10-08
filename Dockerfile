# Assume a linux kernel
FROM python:3.13
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --root-user-action=ignore --upgrade pip
RUN pip3 install --root-user-action=ignore --requirement requirements.txt  
COPY *.py /app
ENTRYPOINT ["python3", "app.py"]
