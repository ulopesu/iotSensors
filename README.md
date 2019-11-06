# IotSensores


## Introdução

Essa é uma api para maninular sensores de usuários.


### Prerequisites

python3.8
pip


### Instalação

INSTALAR PYTHON
    LINUX:
        -executar           sudo apt-get install python3.8
    WINDOWNS
        -baixer e executar  https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe


INSTALAR PIP
    LINUX:
        -executar   sudo apt-get install httpie
    WINDOWNS:
        -baixar    https://bootstrap.pypa.io/get-pip.py
        -executar  python get-pip.py


CRIAR E CONFIGURAR VIRTUAL_ENV
    LINUX
        -executar   python -m venv nome_your_venv
                    nome_your_venv/bin/activate
                    pip install --upgrade django==2.2.7
                    pip install djangorestframework
                   
    WINDOWNS
        -executar:  virtualenv nome_your_venv
                    nome_your_venv\Scripts\activate
                    pip install --upgrade django==2.2.7
                    pip install djangorestframework


INSTALAR HTTPIE
    -executar: pip install --upgrade httpie


## Executando Testes


GET UNITS
    http GET URL_API/units/1/?format=json

GET SENSORS OF USER
    http GET user/USER_ID/getSensors/

GET SENSOR WITH KEY
    http GET URL_API/sensor/KEY_UUID/?format=json

GET STREAM WITH KEY
    http GET URL_API/stream/KEY_UUID/?format=json

POST SENSOR
    http POST URL_API/sensor/  user="URL_API/users/PRIMARY_KEY/" label="Your_Sensor_Label description="Your_Sensor_Description"

POST STREAM IN SENSOR
    http POST URL_API/stream/  sensor="URL_API/sensor/KEY_UUID/" label="Your_Stream_Label" enable=boolean unit=VALUE_OF_UNIT_INT_ENUM

POST DATA IN STREAM
    http POST URL_API/data/  stream="URL_API/stream/KEY_UUID/" timestamp="TIME_FORMAT_UTC" value=VALUE_FLOAT



## Autor

    **Usiel Lopes** -- [ulopesu](https://github.com/ulopesu)


