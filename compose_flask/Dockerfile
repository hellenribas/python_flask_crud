FROM python:3.6
ADD . /coder
WORKDIR /coder
EXPOSE 5000
COPY requirements.txt /coder
RUN pip install -r requirements.txt
COPY app.py /coder
CMD python app.py