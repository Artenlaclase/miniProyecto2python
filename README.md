# Mini Proyecto 2 - Administración de Smartphones

## Descripción

Este proyecto implementa una aplicación web para administrar fabricantes y modelos de smartphones. La aplicación permite gestionar la información sobre diferentes fabricantes y sus respectivos smartphones, facilitando el registro y la visualización de estos datos.

### Características

La aplicación incluye las siguientes funcionalidades:

- **Modelo "Fabricante de Smartphones"**:
  - Nombre
  - País de origen
  - Fecha de fundación
  - Link a página web

- **Modelo "Smartphone"**:
  - Nombre
  - Relación con el "Fabricante de Smartphones"
  - RAM
  - Almacenamiento
  - Tamaño de la pantalla

- **Vistas**:
  - Lista de smartphones agrupados por fabricante.
  - Formulario para registrar un nuevo smartphone.

## Trabajo a Realizar

1. Iniciar un nuevo proyecto Django de acuerdo al tutorial visto en clases.
2. Crear una nueva app Django para implementar la funcionalidad requerida, usando el comando:

    ```bash python manage.py startapp <nombre_de_app>  ```

3. Implementar los modelos solicitados en el archivo models.py de la app.
4. Implementar una vista en views.py que obtenga los smartphones y renderice un template que los muestre agrupados por fabricante.
5. Implementar otra vista en views.py que incluya un ModelForm desde forms.py para permitir el registro de un smartphone.
6. Registrar las rutas necesarias en los archivos urls.py.

### Instalación
Para instalar y ejecutar el proyecto, sigue los siguientes pasos:

1. Clona este repositorio:
 ```bash git clone https://github.com/Artenlaclase/miniProyecto2python.git cd miniProyecto2python ```

2. Crea un entorno virtual (opcional pero recomendado):
   
 ```bash python -m venv venv  source venv/bin/activate  # En Windows usa: venv\Scripts\activate ```
3. Instala las dependencias necesarias:
 ```bash pip install -r requirements.txt ```
4. Realiza las migraciones de la base de datos:
 ```bash python manage.py makemigrations python manage.py migrate ```
5. Ejecuta el servidor de desarrollo:

 ```bash python manage.py runserver ```

6. Abre tu navegador y visita http://127.0.0.1:8000/smartphones/ para acceder a la aplicación.

### Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y asegúrate de que todo funcione correctamente.
4. Envía un pull request describiendo tus cambios.

### Licencia
Este proyecto está licenciado bajo la MIT License.
