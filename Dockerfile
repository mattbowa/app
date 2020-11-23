FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# for psycopg2-binary to work on alpine 
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2-binary

EXPOSE 5000
COPY . .
CMD ["flask", "run"]
