FROM python:3

WORKDIR /usr/src/avtal/backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd avtal
RUN chown -R avtal /usr/src/avtal/backend

USER avtal

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD example
ENV POSTGRES_HOST db
ENV POSTGRES_PORT 5432
ENV POSTGRES_DB postgres

EXPOSE 5000

CMD ["sh", "start.sh"]