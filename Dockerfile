FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirments.txt /app/requirments.txt
RUN pip install -r requirments.txt 
COPY . /app

CMD python main.py