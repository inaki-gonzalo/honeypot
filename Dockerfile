FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY main.py /usr/src/app/
CMD [ "python", "./main.py" ]
