FROM python:3.8-buster
WORKDIR /home/app
COPY server.py .
COPY requirements.txt .
COPY ./model/model.py ./model/
COPY ./model/model.sav ./model/
RUN pip install install-requires
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["server.py"]