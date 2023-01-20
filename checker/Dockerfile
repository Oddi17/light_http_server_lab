FROM ubuntu
RUN apt update
RUN apt install -y python3 python3-pip
RUN pip install requests
WORKDIR /home/service
ADD checker.py /home/service/checker.py
ENTRYPOINT ["python3","checker.py"]
