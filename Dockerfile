FROM python:3.8.10

WORKDIR /app

COPY . /app

RUN apt-get update
RUN apt-get install python3-tk -y
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["/bin/bash"]