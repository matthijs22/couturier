FROM python:3.8-buster-slim
WORKDIR /home/app
COPY app.py .
COPY model_manager.py .
COPY requirements.txt .
COPY models .
RUN pip install install-requires
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]