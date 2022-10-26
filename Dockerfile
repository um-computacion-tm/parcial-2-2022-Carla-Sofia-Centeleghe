FROM python:3

RUN git clone https://github.com/um-computacion-tm/parcial-2-2022-Carla-Sofia-Centeleghe.git

WORKDIR /parcial-2-2022-Carla-Sofia-Centeleghe

RUN pip install -r requirements.txt

CMD ["python3", "test.py"