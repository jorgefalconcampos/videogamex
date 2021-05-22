## Como instalar y correr el proyecto:

----

1) Clonar el repo desde GitHub

2) Localizarse en la carpeta del proyecto > Git Bash here

3) Ejecutar el comando:

```
$ python -m venv vgmx_env 
```

Y darle un nombre al virtual env, en este caso el nombre fue `vgmx_env`

El proceso de creación del ***venv*** solo se hará una vez, posteriormente solo se debe activar


4) Activar el entorno virtual con 

```
$ source vgmx_env/scripts/activate
```


5) Instalar los paquetes requeridos con 
```
$ pip install -r requirements.txt
```
**NOTA**: esto es opcional, pero se puede upgradear *pip* antes del paso #5 con el comando:  `python -m pip install --upgrade pip`

6) Ejecutar las migraciones con: 
```
$ python manage.py migrate
```

7) Iniciar el servidor con
```
python manage.py runserver
```

---
---
---

Cuando se realizen cambios en los modelos: 

1) Generar archivo de migraciones con:

```
python manage.py makemigrations vgmxApp
```



2) Aplicar migraciones a la BDD con con:

```
python manage.py migrate vgmxApp
```