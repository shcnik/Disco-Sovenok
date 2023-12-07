FROM python:3

RUN pip install --upgrade pip
RUN pip install --upgrade Pillow

COPY ./config.py /opt
COPY ./estool-1.001.py /opt
COPY ./sprites-lol.py /opt

CMD ["python3", "./estool-1.001.py"]

