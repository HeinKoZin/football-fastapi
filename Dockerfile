FROM python:3.11.1

LABEL authors="heinkozin"


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY functions /code/app


CMD ["fastapi", "run", "app/main.py", "--port", "80"]