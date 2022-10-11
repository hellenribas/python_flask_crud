FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
ADD . /coder
WORKDIR /coder
EXPOSE 5000
COPY ./app/requirements.txt /coder
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./app/app.py /coder
CMD ["python", "app/app.py"]