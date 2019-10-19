FROM python:3.7

WORKDIR /tmp/
ADD requirements.txt /tmp/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

WORKDIR /etc/app

ADD src/ ./

CMD ["python", "./control.py"]
