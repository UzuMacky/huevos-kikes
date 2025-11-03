# 🛠️ Comandos Útiles - Desarrollo

Este archivo contiene comandos útiles para trabajar con el proyecto durante el desarrollo.

---

## 🔧 Configuración Inicial

### 1. Crear entorno virtual
```powershell
python -m venv venv
```

### 2. Activar entorno virtual
```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
venv\Scripts\activate.bat
```

### 3. Instalar dependencias
```powershell
pip install -r requirements.txt
```

---

## 🗄️ Base de Datos

### Crear migraciones
```powershell
python manage.py makemigrations
```

### Aplicar migraciones
```powershell
python manage.py migrate
```

### Ver SQL de una migración
```powershell
python manage.py sqlmigrate core 0001
```

### Revertir migraciones
```powershell
# Revertir a una migración específica
python manage.py migrate core 0001

# Revertir todas las migraciones de una app
python manage.py migrate core zero
```

### Limpiar base de datos (SQLite)
```powershell
# Eliminar archivo de base de datos
Remove-Item db.sqlite3

# Crear nueva base de datos
python manage.py migrate
python manage.py createsuperuser
```

---

## 👤 Usuarios

### Crear superusuario
```powershell
python manage.py createsuperuser
```

### Cambiar contraseña de usuario
```powershell
python manage.py changepassword admin
```

---

## 🏃 Ejecutar el Servidor

### Servidor de desarrollo
```powershell
python manage.py runserver
```

### Servidor en puerto específico
```powershell
python manage.py runserver 8080
```

### Servidor accesible desde red local
```powershell
python manage.py runserver 0.0.0.0:8000
```

---

## 📊 Datos de Prueba

### Crear tipos de huevo iniciales
```powershell
python manage.py shell
```

```python
from inventario.models import TipoHuevo

TipoHuevo.objects.create(tipo='A', precio_cubeta=25000, stock_cubetas=100)
TipoHuevo.objects.create(tipo='AA', precio_cubeta=30000, stock_cubetas=150)
TipoHuevo.objects.create(tipo='AAA', precio_cubeta=35000, stock_cubetas=80)
```

### Crear proveedor de prueba (sin archivos)
```python
from proveedores.models import Proveedor

Proveedor.objects.create(
    nombre='Granja San José',
    nit='900123456-7',
    direccion='Vereda El Carmen, Km 15',
    telefono='3101234567',
    email='contacto@granjasanjose.com',
    activo=True
)
```

### Crear cliente de prueba
```python
from clientes.models import Cliente

Cliente.objects.create(
    nombre='Tienda Don Pepe',
    cedula_nit='80012345-6',
    direccion='Calle 45 #12-34',
    telefono='3109876543',
    email='donpepe@tienda.com',
    latitud=4.60971,
    longitud=-74.08175,
    activo=True
)
```

### Crear saldo inicial en caja
```python
from core.utils import registrar_transaccion_caja

# Ingreso inicial de capital
registrar_transaccion_caja(
    monto=5000000,
    tipo='ingreso',
    descripcion='Capital inicial de caja'
)
```

---

## 📁 Archivos Estáticos

### Recopilar archivos estáticos
```powershell
python manage.py collectstatic
```

### Recopilar sin confirmación
```powershell
python manage.py collectstatic --noinput
```

### Limpiar archivos estáticos
```powershell
python manage.py collectstatic --clear --noinput
```

---

## 🐳 Docker

### Construir imagen
```powershell
docker build -t huevos-kikes-scm .
```

### Ejecutar con docker-compose
```powershell
docker-compose up
```

### Ejecutar en segundo plano
```powershell
docker-compose up -d
```

### Ver logs
```powershell
docker-compose logs -f
```

### Detener contenedores
```powershell
docker-compose down
```

### Detener y eliminar volúmenes
```powershell
docker-compose down -v
```

### Ejecutar comando en contenedor
```powershell
docker-compose exec web python manage.py migrate
```

### Shell en contenedor
```powershell
docker-compose exec web bash
```

---

## 🔍 Inspección y Debugging

### Shell interactivo de Django
```powershell
python manage.py shell
```

### Shell con imports automáticos
```powershell
python manage.py shell_plus  # Requiere django-extensions
```

### Ver configuración actual
```powershell
python manage.py diffsettings
```

### Verificar configuración del proyecto
```powershell
python manage.py check
```

### Ver estructura de URLs
```powershell
python manage.py show_urls  # Requiere django-extensions
```

---

## 📦 Dependencias

### Actualizar requirements.txt
```powershell
pip freeze > requirements.txt
```

### Instalar paquete y actualizar requirements
```powershell
pip install nombre-paquete
pip freeze > requirements.txt
```

### Ver paquetes instalados
```powershell
pip list
```

### Ver paquetes desactualizados
```powershell
pip list --outdated
```

---

## 🧪 Testing

### Ejecutar todos los tests
```powershell
python manage.py test
```

### Tests de una app específica
```powershell
python manage.py test proveedores
```

### Tests con cobertura
```powershell
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Genera reporte HTML
```

---

## 🔐 Seguridad

### Generar nueva SECRET_KEY
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Verificar vulnerabilidades en dependencias
```powershell
pip install safety
safety check
```

---

## 📄 Gestión de Archivos Media

### Crear directorios necesarios
```powershell
New-Item -Path "media\documentos\proveedores\rut" -ItemType Directory -Force
New-Item -Path "media\documentos\proveedores\camara_comercio" -ItemType Directory -Force
```

---

## 🚀 Preparación para Producción

### Verificar configuración de deployment
```powershell
python manage.py check --deploy
```

### Compilar mensajes de traducción
```powershell
python manage.py compilemessages
```

---

## 📊 Base de Datos PostgreSQL (Local)

### Crear base de datos (usando psql)
```sql
CREATE DATABASE huevos_kikes_db;
CREATE USER huevos_kikes_user WITH PASSWORD 'password';
ALTER ROLE huevos_kikes_user SET client_encoding TO 'utf8';
ALTER ROLE huevos_kikes_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE huevos_kikes_user SET timezone TO 'America/Bogota';
GRANT ALL PRIVILEGES ON DATABASE huevos_kikes_db TO huevos_kikes_user;
```

### Conectar a PostgreSQL
```powershell
psql -U huevos_kikes_user -d huevos_kikes_db
```

### Backup de base de datos
```powershell
# PostgreSQL
pg_dump -U huevos_kikes_user huevos_kikes_db > backup.sql

# SQLite
Copy-Item db.sqlite3 backup_db.sqlite3
```

### Restaurar base de datos
```powershell
# PostgreSQL
psql -U huevos_kikes_user huevos_kikes_db < backup.sql

# SQLite
Copy-Item backup_db.sqlite3 db.sqlite3
```

---

## 🎨 Frontend (Si usas npm/webpack)

### Instalar dependencias frontend
```powershell
npm install
```

### Compilar assets
```powershell
npm run build
```

### Watch mode para desarrollo
```powershell
npm run watch
```

---

## 🔄 Git

### Estado del repositorio
```powershell
git status
```

### Agregar cambios
```powershell
git add .
```

### Commit
```powershell
git commit -m "Descripción de cambios"
```

### Push a GitHub
```powershell
git push origin main
```

### Ver historial
```powershell
git log --oneline
```

---

## 📝 Logs y Debugging

### Ver logs del servidor de desarrollo
Los logs aparecen directamente en la consola donde ejecutas `runserver`.

### Configurar logging en development
Agrega en `settings.py`:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
```

---

## 💡 Tips y Trucos

### Limpiar archivos .pyc
```powershell
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item
Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse
```

### Ver tamaño de base de datos
```powershell
# SQLite
Get-Item db.sqlite3 | Select-Object Name, @{Name="Size(MB)";Expression={$_.Length / 1MB}}
```

### Copiar estructura del proyecto
```powershell
tree /F > estructura_proyecto.txt
```

---

## 🆘 Solución de Problemas Comunes

### Error: "No module named 'X'"
```powershell
pip install -r requirements.txt
```

### Error: "Port 8000 already in use"
```powershell
# Encontrar proceso usando el puerto
Get-NetTCPConnection -LocalPort 8000

# Matar el proceso (reemplaza PID)
Stop-Process -Id PID -Force
```

### Error de migraciones
```powershell
# Eliminar migraciones y empezar de nuevo
Remove-Item -Path "*/migrations/0*.py"
python manage.py makemigrations
python manage.py migrate
```

---

## 📚 Recursos Útiles

- Documentación de Django: https://docs.djangoproject.com/
- Django Best Practices: https://django-best-practices.readthedocs.io/
- Two Scoops of Django: https://www.feldroy.com/books/two-scoops-of-django-3-x

---

**Mantén este archivo a mano durante el desarrollo.** 🚀
