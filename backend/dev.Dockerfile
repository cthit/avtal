FROM python:3

WORKDIR /usr/src/avtal/backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd avtal
RUN chown -R avtal /usr/src/avtal/backend

USER avtal

EXPOSE 8080

CMD ["sh", "start.sh"]