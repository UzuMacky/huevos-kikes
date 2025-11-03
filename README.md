# Sistema SCM - Huevos Kikes 🥚

Sistema de gestión de cadena de suministro (Supply Chain Management) para Huevos Kikes, desarrollado con Django.

## 📋 Descripción

Sistema completo para la gestión de:
- **Proveedores**: Gestión con documentos (RUT, Cámara de Comercio)
- **Clientes**: Con geolocalización (Google Maps)
- **Inventario**: Control de tipos de huevo (A, AA, AAA) con stock
- **Ventas**: Con generación de facturas en PDF
- **Compras**: Con validación de saldo en caja
- **Caja**: Dashboard con control de ingresos y egresos

## 🚀 Stack Tecnológico

- **Backend**: Python 3.10+
- **Framework**: Django 4.x
- **Base de Datos**: PostgreSQL
- **Servidor**: Gunicorn
- **Contenedores**: Docker
- **Despliegue**: Render

## 📦 Instalación Local

### Prerrequisitos

- Python 3.10 o superior
- PostgreSQL (opcional, se puede usar SQLite para desarrollo)
- Git

### Pasos

1. **Clonar el repositorio**
```bash
git clone <url-del-repositorio>
cd huevos_kikes_scm
```

2. **Crear entorno virtual**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**

Copiar el archivo de ejemplo y configurar:
```bash
cp .env.example .env
```

Editar `.env` con tus valores:
```env
# Django
SECRET_KEY=tu-secret-key-aqui
DEBUG=True

# Base de datos (opcional, usa SQLite por defecto)
# DATABASE_URL=postgresql://usuario:password@localhost:5432/huevos_kikes_db

# Google Maps API (REQUERIDO para geolocalización)
GOOGLE_MAPS_API_KEY=tu-api-key-de-google-maps

# Email (opcional)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

**Nota**: Para obtener tu Google Maps API Key, sigue la guía en la [documentación de Google Maps](https://developers.google.com/maps/documentation/javascript/get-api-key).

5. **Ejecutar migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crear superusuario**
```bash
python manage.py createsuperuser
```

7. **Cargar datos iniciales (opcional)**
```bash
# Crear tipos de huevo
python manage.py shell -c "
from inventario.models import TipoHuevo
TipoHuevo.objects.create(tipo='A', precio_venta_cubeta=25000, stock_cubetas=0)
TipoHuevo.objects.create(tipo='AA', precio_venta_cubeta=30000, stock_cubetas=0)
TipoHuevo.objects.create(tipo='AAA', precio_venta_cubeta=35000, stock_cubetas=0)
print('Tipos de huevo creados')
"

# Crear saldo inicial en caja
python manage.py shell -c "
from core.utils import registrar_transaccion_caja
registrar_transaccion_caja(monto=5000000, tipo='ingreso', descripcion='Capital inicial de caja')
print('Saldo inicial: $5,000,000 COP')
"
```

8. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

Visita: http://localhost:8000

## 🐳 Despliegue con Docker (Desarrollo)

1. **Construir y ejecutar contenedores**
```bash
docker-compose up --build
```

2. **Ejecutar migraciones dentro del contenedor**
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

3. **Acceder a la aplicación**
```
http://localhost:8000
```

## 🌐 Despliegue en Render

### 1. Preparación

1. Sube tu código a un repositorio de GitHub
2. Crea una cuenta en [Render](https://render.com)

### 2. Crear PostgreSQL Database

1. En el dashboard de Render, crea un nuevo **PostgreSQL** database
2. Copia la **Internal Database URL**

### 3. Crear Web Service

1. Crea un nuevo **Web Service** desde el repositorio de GitHub
2. Configura:
   - **Name**: `huevos-kikes-scm`
   - **Environment**: `Docker`
   - **Region**: Elige la más cercana
   - **Branch**: `main` (o tu rama principal)

3. **Variables de Entorno**:
   ```
   SECRET_KEY=<genera-una-secret-key-segura>
   DEBUG=False
   DATABASE_URL=<internal-database-url-de-render>
   PYTHONVERSION=3.10
   ```

   Para generar SECRET_KEY:
   ```python
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

4. **Deploy**

Render detectará automáticamente el `Dockerfile` y construirá la imagen.

### 4. Ejecutar comandos post-deploy

Una vez desplegado, ejecuta desde la consola de Render:

```bash
python manage.py migrate
python manage.py createsuperuser
```

## 📁 Estructura del Proyecto

```
huevos_kikes_scm/
├── core/                   # Autenticación y Dashboard
├── proveedores/           # Gestión de proveedores
├── clientes/              # Gestión de clientes
├── inventario/            # Gestión de inventario
├── transacciones/         # Ventas y compras
├── templates/             # Templates HTML
├── static/                # Archivos estáticos (CSS, JS)
├── media/                 # Archivos subidos
├── huevos_kikes_scm/     # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── manage.py
```

## 🔧 Configuración de Archivos Media (Producción)

Los archivos subidos en Render son **efímeros** (se pierden al redeployar). Para producción, usa AWS S3:

### 1. Crear bucket en AWS S3

1. Crea un bucket en S3
2. Configura CORS y permisos públicos

### 2. Instalar django-storages

Ya está en `requirements.txt` (descomenta las líneas)

### 3. Configurar variables de entorno en Render

```env
AWS_ACCESS_KEY_ID=<tu-access-key>
AWS_SECRET_ACCESS_KEY=<tu-secret-key>
AWS_STORAGE_BUCKET_NAME=<nombre-bucket>
AWS_S3_REGION_NAME=us-east-1
```

### 4. Descomentar configuración S3 en settings.py

```python
if not DEBUG:
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    # ... resto de la configuración
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

## 📧 Configuración de Email (Recuperación de contraseña)

Para producción, configura un servicio SMTP (ej. SendGrid, Gmail):

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-app-password
DEFAULT_FROM_EMAIL=tu-email@gmail.com
```

## 🗺️ Integración Google Maps (Clientes)

Para usar la funcionalidad de geolocalización en el módulo de clientes:

1. Obtén una API Key de Google Maps en [Google Cloud Console](https://console.cloud.google.com/)
2. Habilita las APIs: Maps JavaScript API, Geocoding API
3. Agrega la API Key en tus templates de clientes

Ejemplo en `templates/clientes/cliente_form.html`:
```html
<script src="https://maps.googleapis.com/maps/api/js?key=TU_API_KEY&callback=initMap" async defer></script>
```

## 📊 Funcionalidades Principales

### Módulo 0: Autenticación
- Login/Logout
- Recuperación de contraseña
- Dashboard con saldo en caja

### Módulo 1: Proveedores
- CRUD completo
- Validación de documentos (RUT, Cámara de Comercio)
- Archivos adjuntos

### Módulo 2: Clientes
- CRUD completo
- Geolocalización con Google Maps
- Captura de coordenadas

### Módulo 3: Inventario
- Tipos de huevo (A, AA, AAA)
- Control de stock
- Exportación a Excel

### Módulo 4: Ventas
- Formsets para múltiples productos
- Validación de stock
- Generación de facturas PDF
- Registro automático en caja

### Módulo 5: Compras
- Formsets para múltiples productos
- Validación de saldo en caja
- Actualización automática de stock
- Registro automático en caja

### Módulo 6: Saldo en Caja
- Dashboard con saldo actual
- Historial de ingresos
- Historial de egresos
- Totales acumulados

## 🧪 Próximos Pasos

1. **Crear templates HTML** para todas las vistas
2. **Agregar estilos CSS** (Bootstrap recomendado)
3. **Implementar JavaScript** para formsets dinámicos
4. **Configurar Google Maps** en formulario de clientes
5. **Diseñar template de factura PDF**
6. **Configurar AWS S3** para archivos en producción
7. **Agregar pruebas unitarias**

## 📝 Notas Importantes

- Los archivos media son **efímeros en Render** - usa S3 en producción
- Cambia `SECRET_KEY` en producción
- Configura `ALLOWED_HOSTS` según tu dominio
- Usa variables de entorno para información sensible
- Ejecuta `collectstatic` antes de desplegar

## 👨‍💻 Desarrollo

Para agregar nuevas funcionalidades:

1. Crea la app: `python manage.py startapp nombre_app`
2. Agrega a `INSTALLED_APPS` en `settings.py`
3. Crea modelos en `models.py`
4. Crea migraciones: `python manage.py makemigrations`
5. Aplica migraciones: `python manage.py migrate`
6. Registra en `admin.py`

## 📄 Licencia

Proyecto académico - UNIMINUTO

---

**Desarrollado para**: Parcial Tercer Corte - Sistemas de Información  
**Cliente**: Huevos Kikes  
**Universidad**: UNIMINUTO
