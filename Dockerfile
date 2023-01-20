FROM ubuntu
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install flask
WORKDIR /home/service
ENTRYPOINT python3 sitejson.py
