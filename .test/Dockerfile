FROM python:3

RUN pip install --upgrade pip
RUN pip install --upgrade Pillow

COPY .test/config.py /opt
COPY .test/estool-1.001.py /opt
COPY .test/sprites_lol.rpy /opt
COPY . /home/src

CMD ["ls", "-l", "/home/src"]
CMD ["python3", "/opt/estool-1.001.py"]

