# bookstore

## 1°) Crear entorno virtual para instalar dependencias.
### En **Linux**
```bash
$ git clone https://github.com/tom-villanueva/weblibreria.git
$ cd bookstore
$ python3 -m virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requerimientos.txt
(venv) $ #Actualizar pip si es necesario con:
(venv) $ python3 -m pip install --upgrade pip
```
### En **Windows**
```cmd
$ git clone https://github.com/tom-villanueva/weblibreria.git
$ cd weblibreria
$ python3 -m virtualenv venv
$ source venv/bin/activate                                      //en windows: venv\Scripts\activate.bat
(venv) $ pip install -r requerimientos.txt
(venv) $ #Actualizar pip si es necesario con:
(venv) $ python3 -m pip install --upgrade pip
```

## 2°) Ejecutar con el manage.py que se encuentra en src.
```bash
(venv) $ cd src
(venv) $ python3 manage.py makemigrations
(venv) $ python3 manage.py migrate
(venv) $ python3 manage.py runserver
```

## 3°) Abrir sitio en navegador
Abrir un navegador de internet y dirigirse al sitio: *http://127.0.0.1:8000/*