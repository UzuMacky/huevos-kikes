# 🚀 Guía de Despliegue en Render

Esta guía te llevará paso a paso para desplegar el sistema SCM de Huevos Kikes en Render.

## 📋 Pre-requisitos

- [ ] Cuenta en [GitHub](https://github.com)
- [ ] Cuenta en [Render](https://render.com)
- [ ] Código del proyecto subido a un repositorio de GitHub

---

## 🔑 Paso 1: Generar SECRET_KEY

Antes de comenzar, genera una clave secreta segura para Django:

### Opción A: Usando Python
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Opción B: Generador en línea
Visita: https://djecrety.ir/

**Guarda esta clave** - la necesitarás más adelante.

---

## 💾 Paso 2: Crear Base de Datos PostgreSQL en Render

1. **Inicia sesión en Render**: https://dashboard.render.com/

2. **Crear nuevo PostgreSQL Database**:
   - Click en **"New +"** → **"PostgreSQL"**

3. **Configurar la base de datos**:
   - **Name**: `huevos-kikes-db` (o el nombre que prefieras)
   - **Database**: `huevos_kikes_db`
   - **User**: `huevos_kikes_user` (se genera automáticamente)
   - **Region**: Selecciona la región más cercana a tus usuarios
   - **Plan**: Free (para desarrollo/pruebas)

4. **Crear Database**:
   - Click en **"Create Database"**
   - Espera a que se complete la creación (puede tomar unos minutos)

5. **Copiar la Internal Database URL**:
   - Una vez creada, ve a la pestaña **"Info"**
   - Copia el valor de **"Internal Database URL"** (comienza con `postgresql://...`)
   - **Formato**: `postgresql://user:password@host:port/database`
   - ⚠️ **MUY IMPORTANTE**: Usa la **Internal URL**, NO la External URL

---

## 🌐 Paso 3: Crear Web Service en Render

1. **Crear nuevo Web Service**:
   - En el dashboard de Render, click en **"New +"** → **"Web Service"**

2. **Conectar repositorio de GitHub**:
   - Si es la primera vez, conecta tu cuenta de GitHub
   - Selecciona el repositorio `huevos_kikes_scm`
   - Click en **"Connect"**

3. **Configurar el servicio**:
   
   | Campo | Valor |
   |-------|-------|
   | **Name** | `huevos-kikes-scm` |
   | **Region** | Misma región que la base de datos |
   | **Branch** | `main` (o tu rama principal) |
   | **Runtime** | `Docker` |
   | **Plan** | Free (para desarrollo) |

4. **No modifiques** las opciones de Build Command o Start Command (Docker las maneja automáticamente)

---

## ⚙️ Paso 4: Configurar Variables de Entorno

En la sección **"Environment"** del Web Service, agrega las siguientes variables:

### Variables Requeridas:

```env
SECRET_KEY=<tu-secret-key-generada-en-paso-1>
DEBUG=False
DATABASE_URL=<internal-database-url-del-paso-2>
PYTHONVERSION=3.10
```

### Ejemplo Real:
```env
SECRET_KEY=django-insecure-tu-clave-super-secreta-aqui-123456789
DEBUG=False
DATABASE_URL=postgresql://huevos_kikes_user:password123@dpg-xxxx-a.oregon-postgres.render.com:5432/huevos_kikes_db
PYTHONVERSION=3.10
```

### Variables Opcionales (Email):
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-app-password
DEFAULT_FROM_EMAIL=tu-email@gmail.com
```

**Nota sobre Gmail**: Si usas Gmail, necesitas generar una "App Password" en tu cuenta de Google (no uses tu contraseña normal).

### Variables para Google Maps:
```env
GOOGLE_MAPS_API_KEY=tu-api-key-de-google-maps
```

**Importante**: Asegúrate de restringir tu API Key de Google Maps solo a tu dominio de Render en Google Cloud Console.

---

## 🚀 Paso 5: Desplegar

1. **Iniciar el despliegue**:
   - Click en **"Create Web Service"**
   - Render comenzará a construir la imagen Docker

2. **Proceso de Build**:
   - Render detectará el `Dockerfile`
   - Instalará dependencias (puede tomar 5-10 minutos la primera vez)
   - Ejecutará `collectstatic`
   - Iniciará Gunicorn

3. **Monitorear el proceso**:
   - Ve a la pestaña **"Logs"** para ver el progreso
   - Busca mensajes como:
     ```
     Building...
     Successfully built
     Starting service...
     Gunicorn started
     ```

4. **Esperar a que el estado sea "Live"**:
   - Cuando veas un círculo verde y "Live", el despliegue fue exitoso

---

## 🗄️ Paso 6: Ejecutar Migraciones

Una vez desplegado, necesitas crear las tablas en la base de datos:

1. **Abrir Shell**:
   - En tu Web Service, ve a la pestaña **"Shell"**
   - Click en **"Launch Shell"** (puede tardar un momento)

2. **Ejecutar migraciones**:
   ```bash
   python manage.py migrate
   ```

3. **Crear superusuario**:
   ```bash
   python manage.py createsuperuser
   ```
   
   Te pedirá:
   - Username (ej: admin)
   - Email (ej: admin@huevoskikes.com)
   - Password (elige una segura)
   - Password confirmation

4. **Crear tipos de huevo iniciales** (opcional):
   ```bash
   python manage.py shell
   ```
   
   Luego en el shell de Python:
   ```python
   from inventario.models import TipoHuevo
   
   TipoHuevo.objects.create(tipo='A', precio_cubeta=25000, stock_cubetas=0)
   TipoHuevo.objects.create(tipo='AA', precio_cubeta=30000, stock_cubetas=0)
   TipoHuevo.objects.create(tipo='AAA', precio_cubeta=35000, stock_cubetas=0)
   
   exit()
   ```

---

## ✅ Paso 7: Verificar el Despliegue

1. **Obtener la URL**:
   - En la parte superior del dashboard, verás una URL como:
   - `https://huevos-kikes-scm.onrender.com`

2. **Probar la aplicación**:
   - Visita: `https://tu-app.onrender.com/admin`
   - Inicia sesión con el superusuario creado
   - Verifica que puedas acceder al panel de administración

3. **Probar el login**:
   - Visita: `https://tu-app.onrender.com/login/`
   - Inicia sesión con tus credenciales

---

## 📁 Paso 8: Configurar Archivos Media (AWS S3)

⚠️ **IMPORTANTE**: Los archivos subidos en Render se **borrarán** cada vez que redespliegues.

Para archivos permanentes (documentos de proveedores, etc.), necesitas AWS S3:

### 8.1. Crear Bucket en AWS S3

1. **Crear cuenta en AWS**: https://aws.amazon.com/
2. **Ir a S3**: Console → S3
3. **Create Bucket**:
   - Nombre: `huevos-kikes-media` (debe ser único globalmente)
   - Region: us-east-1 (o la más cercana)
   - Desbloquear acceso público
   - Create bucket

4. **Configurar CORS**:
   - En el bucket, ve a **Permissions** → **CORS**
   - Agrega:
   ```json
   [
       {
           "AllowedHeaders": ["*"],
           "AllowedMethods": ["GET", "POST", "PUT"],
           "AllowedOrigins": ["*"],
           "ExposeHeaders": []
       }
   ]
   ```

### 8.2. Crear IAM User para S3

1. **IAM Console**: https://console.aws.amazon.com/iam/
2. **Users** → **Add User**:
   - Username: `huevos-kikes-s3-user`
   - Access type: Programmatic access
3. **Permissions**:
   - Attach existing policies: `AmazonS3FullAccess`
4. **Guardar las credenciales**:
   - Access Key ID
   - Secret Access Key

### 8.3. Configurar en Render

Agrega estas variables de entorno en tu Web Service:

```env
AWS_ACCESS_KEY_ID=<tu-access-key-id>
AWS_SECRET_ACCESS_KEY=<tu-secret-access-key>
AWS_STORAGE_BUCKET_NAME=huevos-kikes-media
AWS_S3_REGION_NAME=us-east-1
```

### 8.4. Descomentar configuración en settings.py

En `settings.py`, descomenta las líneas:

```python
if not DEBUG:
    # AWS S3 Settings
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    # ... resto del código
```

Haz commit y push. Render redespliegará automáticamente.

---

## 🔄 Redeployar Cambios

Cada vez que hagas cambios en tu código:

1. **Commit y Push a GitHub**:
   ```bash
   git add .
   git commit -m "Descripción de cambios"
   git push origin main
   ```

2. **Render redespliegue automáticamente**:
   - Render detecta cambios en GitHub
   - Reconstruye la imagen Docker
   - Despliega la nueva versión
   - **Nota**: Esto puede tomar 5-10 minutos

3. **Ejecutar migraciones si hay cambios en modelos**:
   - Shell → `python manage.py migrate`

---

## 🐛 Solución de Problemas

### Error: "Application failed to start"

**Solución**:
1. Revisa los logs en Render
2. Verifica que `DATABASE_URL` esté correcta (usa Internal URL)
3. Verifica que todas las variables de entorno estén configuradas

### Error: "relation does not exist"

**Solución**:
1. No ejecutaste las migraciones
2. Abre Shell y ejecuta: `python manage.py migrate`

### Error: "ALLOWED_HOSTS"

**Solución**:
1. Verifica que en `settings.py` tengas:
   ```python
   ALLOWED_HOSTS = ['*.onrender.com', 'localhost', '127.0.0.1']
   ```

### La aplicación está lenta en el plan Free

**Explicación**:
- El plan Free de Render "duerme" después de 15 minutos de inactividad
- La primera solicitud después de dormir tarda ~30 segundos
- **Solución**: Actualiza al plan Starter ($7/mes) para servicio 24/7

### Los archivos subidos desaparecen

**Explicación**:
- Los archivos en Render son efímeros
- **Solución**: Configura AWS S3 (Paso 8)

---

## 📊 Monitoreo

### Ver Logs en Tiempo Real

1. Dashboard → Tu Web Service
2. Pestaña **"Logs"**
3. Click en **"Live Logs"**

### Ver Métricas

1. Pestaña **"Metrics"**
2. Verás:
   - CPU usage
   - Memory usage
   - Request count
   - Response time

---

## 💰 Costos

### Plan Free (Desarrollo)
- **Web Service**: $0 (con limitaciones)
- **PostgreSQL**: $0 (hasta 90 días, luego $7/mes)
- **Limitaciones**:
  - Se duerme después de 15 min de inactividad
  - 750 horas/mes de compute

### Plan Starter (Recomendado para Producción)
- **Web Service**: $7/mes
- **PostgreSQL**: $7/mes
- **Total**: ~$14/mes
- **Beneficios**:
  - 24/7 uptime
  - Más recursos
  - Sin sleep

---

## 🎓 Recursos Adicionales

- **Documentación Render**: https://render.com/docs
- **Django Deployment Checklist**: https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
- **Render Django Tutorial**: https://render.com/docs/deploy-django

---

## ✅ Checklist Final

Antes de entregar tu proyecto, verifica:

- [ ] La aplicación está desplegada y accesible
- [ ] El admin de Django funciona
- [ ] Puedes crear usuarios
- [ ] Puedes crear proveedores, clientes, inventario
- [ ] Las ventas y compras funcionan
- [ ] La factura PDF se genera correctamente
- [ ] El dashboard muestra el saldo en caja
- [ ] Los archivos media están en S3 (si configuraste)
- [ ] Las variables de entorno están correctamente configuradas
- [ ] DEBUG=False en producción
- [ ] SECRET_KEY es segura y diferente a la de desarrollo

---

## 📝 Entrega del Proyecto

Incluye en tu entrega:

1. **URL de la aplicación desplegada**
2. **Credenciales de acceso** (usuario y contraseña de prueba)
3. **Repositorio de GitHub** (con README.md)
4. **Documentación** de las funcionalidades implementadas
5. **Video demo** (opcional pero recomendado)

---

**¡Felicidades! Tu sistema SCM de Huevos Kikes está desplegado en producción.** 🎉
