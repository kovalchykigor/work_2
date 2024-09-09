FROM python:3.11.9

WORKDIR /app

# copy from work dir to container
COPY . /app

RUN pip install -r requirements.txt

CMD ["pytest", "--maxfail=1", "--disable-warnings", "--tb=short"]
