FROM python:3.7.2-alpine

RUN pip install --upgrade pip

RUN adduser -D worker
USER worker
WORKDIR /home/worker

RUN pip install --user pipenv

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=worker:worker Pipfile Pipfile
RUN pipenv lock -r > requirements.txt
RUN pip install --user -r requirements.txt

COPY . .

CMD ["python", "twitter-bot.py", "example.txt", "10"]
