FROM python:3.8-slim-buster
WORKDIR /home/app
COPY app.py .
COPY model_manager.py .
COPY config_manager.py .
COPY requirements.txt .
COPY ./models/. ./models/
RUN pip install install-requires
RUN pip install -r requirements.txt
COPY config.yml .
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]