FROM python:3.8.10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
# RUN sudo apt-get install python3-tk

EXPOSE 80

CMD ["/bin/bash"]