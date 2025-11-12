# 🛡️ Implementación de Captcha en Login

## 📋 Resumen

Se ha implementado **django-simple-captcha** en el formulario de login para proteger la aplicación contra ataques automatizados de bots y fuerza bruta.

---

## ✨ Características Implementadas

### 1. **Captcha Visual**
- ✅ Imagen con caracteres aleatorios
- ✅ Tamaño personalizado: 150x50 píxeles
- ✅ 6 caracteres alfanuméricos
- ✅ Rotación de letras entre -20° y 20°
- ✅ Ruido de puntos para mayor seguridad
- ✅ Colores personalizados (fondo blanco, texto azul oscuro)

### 2. **Validación de Seguridad**
- ✅ Tiempo de expiración: 5 minutos
- ✅ Validación del lado del servidor
- ✅ Regeneración automática por cada intento
- ✅ Mensajes de error personalizados

### 3. **Interfaz de Usuario**
- ✅ Integración con Bootstrap 5
- ✅ Diseño responsivo
- ✅ Botón de recarga de captcha
- ✅ Instrucciones claras para el usuario
- ✅ Estilos personalizados para mejor UX

---

## 🛠️ Archivos Modificados

### 1. **requirements.txt**
```txt
# ===== Seguridad =====
django-simple-captcha>=0.6.0  # Captcha para formularios
```

### 2. **settings.py**
```python
INSTALLED_APPS = [
    ...
    'captcha',  # django-simple-captcha
]

# Configuración de django-simple-captcha
CAPTCHA_IMAGE_SIZE = (150, 50)
CAPTCHA_FONT_SIZE = 30
CAPTCHA_LETTER_ROTATION = (-20, 20)
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
CAPTCHA_FOREGROUND_COLOR = '#001F3F'
CAPTCHA_LENGTH = 6
CAPTCHA_TIMEOUT = 5
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots',)
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
```

### 3. **urls.py (Principal)**
```python
urlpatterns = [
    ...
    path('captcha/', include('captcha.urls')),
]
```

### 4. **core/forms.py** (NUEVO)
```python
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField

class LoginFormWithCaptcha(AuthenticationForm):
    captcha = CaptchaField(
        label='Verificación de seguridad',
        help_text='Ingrese los caracteres que ve en la imagen',
        error_messages={
            'invalid': 'El código de verificación es incorrecto. Inténtelo de nuevo.',
            'required': 'Por favor ingrese el código de verificación.',
        }
    )
```

### 5. **core/views.py**
```python
from .forms import LoginFormWithCaptcha

class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    form_class = LoginFormWithCaptcha  # ← Formulario con captcha
    redirect_authenticated_user = True
```

### 6. **templates/core/login.html**
- ✅ Agregado campo de captcha con estilos Bootstrap
- ✅ CSS personalizado para la imagen del captcha
- ✅ Botón de recarga de captcha
- ✅ Mensajes de ayuda y error

---

## 🔧 Instalación y Configuración

### Paso 1: Instalar Dependencias
```bash
pip install django-simple-captcha
```

### Paso 2: Ejecutar Migraciones
```bash
python manage.py migrate
```
Esto crea las tablas necesarias:
- `captcha_captchastore` - Almacena los captchas generados

### Paso 3: Probar
1. Iniciar el servidor: `python manage.py runserver`
2. Ir a: `http://127.0.0.1:8000/`
3. Intentar iniciar sesión
4. Verificar que aparece el captcha

---

## 🎯 Beneficios de Seguridad

### ✅ **Protección contra Bots**
Los scripts automatizados no pueden resolver el captcha visual, evitando ataques masivos.

### ✅ **Prevención de Fuerza Bruta**
Dificulta significativamente los intentos automatizados de adivinar contraseñas.

### ✅ **Validación del Lado del Servidor**
La validación ocurre en el servidor, no en el cliente, evitando bypass con JavaScript.

### ✅ **Expiración Temporal**
Los captchas expiran en 5 minutos, obligando a regenerarlos.

### ✅ **Sin Dependencias Externas**
No requiere servicios de terceros como reCAPTCHA (sin APIs de Google).

---

## 🔍 Cómo Funciona

1. **Usuario accede al login**
   - Django genera un captcha único
   - Se almacena en la base de datos con un hash
   - Se muestra la imagen al usuario

2. **Usuario ingresa credenciales + captcha**
   - Django valida el captcha contra la base de datos
   - Si es correcto, valida username/password
   - Si el captcha falla, rechaza el login

3. **Regeneración automática**
   - Cada intento genera un nuevo captcha
   - Los captchas antiguos expiran automáticamente

---

## 📊 Configuración Personalizable

### Cambiar Dificultad
```python
# Más difícil
CAPTCHA_LENGTH = 8  # 8 caracteres
CAPTCHA_LETTER_ROTATION = (-35, 35)  # Más rotación
CAPTCHA_NOISE_FUNCTIONS = (
    'captcha.helpers.noise_dots',
    'captcha.helpers.noise_arcs',
)

# Más fácil
CAPTCHA_LENGTH = 4  # 4 caracteres
CAPTCHA_LETTER_ROTATION = (-10, 10)  # Menos rotación
```

### Cambiar a Captcha Matemático
```python
# En lugar de letras, usa operaciones matemáticas simples
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
# Ejemplo: "2 + 3 = ?" → Usuario ingresa "5"
```

### Cambiar Colores
```python
CAPTCHA_BACKGROUND_COLOR = '#f0f0f0'  # Gris claro
CAPTCHA_FOREGROUND_COLOR = '#dc3545'  # Rojo Bootstrap
```

---

## 🧪 Pruebas Recomendadas

### ✅ **Test 1: Captcha Correcto**
1. Ingresar usuario y contraseña correctos
2. Resolver el captcha correctamente
3. ✅ Debe permitir el acceso

### ✅ **Test 2: Captcha Incorrecto**
1. Ingresar usuario y contraseña correctos
2. Ingresar captcha incorrecto
3. ✅ Debe rechazar el login con mensaje de error

### ✅ **Test 3: Recarga de Captcha**
1. Hacer clic en "Recargar"
2. ✅ Debe generar un nuevo captcha

### ✅ **Test 4: Expiración**
1. Cargar el login
2. Esperar 6 minutos
3. Intentar login
4. ✅ Debe requerir nuevo captcha

---

## 📝 Notas Importantes

### Para Desarrollo
- El captcha funciona en modo DEBUG=True
- No requiere configuración adicional

### Para Producción
- ✅ Ya está configurado
- ✅ Funciona automáticamente
- ✅ Los captchas se almacenan en la misma base de datos (PostgreSQL)
- ⚠️ Asegúrate de que las tablas de captcha se migren en Render

### Comando para Producción (Render)
```bash
# Ejecutar después del deploy
python manage.py migrate
```

---

## 🚀 Alternativas Futuras

Si necesitas **mayor seguridad** o **mejor UX**:

### 1. **Google reCAPTCHA v3**
- Invisible para el usuario
- Puntuación de riesgo automática
- Requiere API key de Google

### 2. **hCaptcha**
- Alternativa a reCAPTCHA
- Respeta más la privacidad
- Requiere cuenta en hCaptcha

### 3. **Rate Limiting**
- Limitar intentos de login por IP
- Complementa el captcha
- Usa `django-ratelimit`

---

## ✅ Checklist de Implementación

- [x] Agregar django-simple-captcha a requirements.txt
- [x] Configurar settings.py
- [x] Agregar URL de captcha
- [x] Crear LoginFormWithCaptcha
- [x] Actualizar CustomLoginView
- [x] Modificar template de login
- [x] Agregar estilos CSS
- [x] Ejecutar migraciones
- [x] Probar en desarrollo
- [ ] Probar en producción (Render)
- [ ] Documentar en README.md

---

## 📚 Referencias

- **Documentación oficial**: https://django-simple-captcha.readthedocs.io/
- **GitHub**: https://github.com/mbi/django-simple-captcha
- **Django Authentication**: https://docs.djangoproject.com/en/4.2/topics/auth/

---

**Fecha de implementación**: 2025-11-12  
**Desarrollado por**: Equipo Huevos Kikes SCM  
**Versión**: 1.0.0
